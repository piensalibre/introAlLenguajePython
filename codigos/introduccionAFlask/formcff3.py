from wtforms import Form,validators,PasswordField,StringField

def largo(form,field):
     if len(field.data)>0:
          raise validators.ValidationError("El campo debe estar vacio.")

class LoginForm(Form):
     username = StringField('username',
          [
               validators.Required(message="usuario requerido"),
               validators.length(min=4,max=25,message="ingrese un nombre de usuario valido")
          ])
     password = PasswordField('Password',
          [
               validators.Required(message="password requerido"),
               validators.Required(message="email requerido")
          ])