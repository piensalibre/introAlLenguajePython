from wtforms import Form,validators,PasswordField,StringField,HiddenField
from wtforms.fields.simple import TextField
from wtforms.fields.html5 import EmailField
from models import User

def largo(form,field):
     if len(field.data)>0:
          raise validators.ValidationError("El campo debe estar vacio.")

class CommentForm(Form):
     
     comment = TextField('Texto',[
          validators.Required(message="campo requerido")
     ])
     senuelo = HiddenField('',[largo] )

class LoginForm(Form):
     username = StringField('username',
          [
               validators.Required(message="usuario requerido"),
               validators.length(min=4,max=25,message="ingrese un nombre de usuario valido")
          ])
     password = PasswordField('Password',
          [
               validators.Required(message="password requerido")
          ])

class CreateForm(Form):
     username = TextField("Username",[
          validators.Required(message="El usuario es requerido"),
          validators.length(min=4,max=50,message="Ingrese un usuario valido")
     ])
     email = EmailField("Correo electronico",[
          validators.Required(message="El email es requerido"),
          validators.length(min=4,max=50,message="Ingrese un email")
     ])
     password = PasswordField("Password",[
          validators.Required(message="El password es invalido")
     ])

     def validate_username(form,field):
          username = field.data
          user = User.query.filter_by(username=username).first()
          if user is not None:
               raise validators.ValidationError("El usuario ya existe")
