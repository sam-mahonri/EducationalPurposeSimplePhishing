from flask_wtf import FlaskForm # importa a classe FlaskForm do módulo flask_wtf
from wtforms.fields import EmailField, PasswordField # importa os tipos de campos do wtforms que trabalha junto do flask_wtf
from wtforms.validators import InputRequired

class Login(FlaskForm):
    email = EmailField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
