import functools#set de funciones

from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)#importamos Blueprint para crear blueprints que despues podremos configurar a nuestro gusto, flash nos sirve para mandar mensajes de manera generica a nuestras plantillas, g es nuestra variable donde podremos poner valores y acceder a ellos a traves de toda nuestra aplicacion, render_template nos servira para renderizar nuestras plantillas, request para manejar nuestros formularios, url_for para crear nuestras urls, session para mantener la sesion del usuario que se encuentra interactuando dentro del contexto de nuestra aplicacion, redirect para redireccionar a html

from werkzeug.security import check_password_hash, generate_password_hash#estas funciones nos serviran para comprobar si dos contrasenas son iguales y para encriptar nuestras contrasenas

from porHacer.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')#creamos nuestro blueprint que se llamara de nombre auth que recibe el nombre de nuestro archivo y le damos el prefijo /auth a nuestras rutas

@bp.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select id from user where username = %s',(username,)
        )
        if not username:
            error = 'Username es requerido'
        if not password:
            error = 'Password es requerido'
        elif c.fetchone() is not None:
            error = 'Usuario {} se encuentra registrado.'.format(username)
        
        if error is None:
            c.execute(
                'insert into user (username,password) values (%s,%s)',
                (username,generate_password_hash(password))
            )
            db.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db,c = get_db()
        error = None
        c.execute(
            'select * from user where username = %s', (username,)
        )
        user = c.fetchone()

        if user is None:
            error = 'Usuario y/o contrasena invalida'
        elif not check_password_hash(user['password'], password):
            error = 'Usuario y/o contrasena invalida'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('todo.index'))
            
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request#esto se va a ejecutar antes de cada peticion
def load_logged_in_user():#aqui se asigna el valor a g.user, se carga al usuario al contexto de nuestra aplicacion
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from user where id = %s',(user_id,)
        )
        g.user = c.fetchone()

def login_required(view):#en este bloque creamos un decorador que protejera el acceso a las rutas de usuarios que no inicien sesion
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))