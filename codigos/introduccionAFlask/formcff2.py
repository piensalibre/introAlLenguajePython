from wtforms import Form,validators,HiddenField
from wtforms import StringField, TextField 
from wtforms.fields.html5 import EmailField

def largo(form,field):
     if len(field.data)>0:
          raise validators.ValidationError("El campo debe estar vacio.")

class CommentForm(Form):
     username = StringField('username',
          [
               validators.Required(message="usuario requerido"),
               validators.length(min=4,max=25,message="ingrese un nombre de usuario valido")
          ])
     email = EmailField('Correo electronico',
          [
               validators.Required(message="email requerido")
          ])
     comment = TextField('Texto')
     senuelo = HiddenField('',[largo] )