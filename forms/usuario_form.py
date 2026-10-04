from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class UsuarioForm(FlaskForm):
    usuario = StringField(
        'Usuario',
        validators=[
            DataRequired(message='El nombre de usuario es obligatorio.'),
            Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres.')
        ]
    )

    email = EmailField(
        'Correo Electrónico',
        validators=[
            DataRequired(message='El correo electrónico es obligatorio.'),
            Email(message='Ingrese una dirección de correo válida.')
        ]
    )

    password = PasswordField(
        'Contraseña',
        validators=[
            DataRequired(message='La contraseña es obligatoria.'),
            Length(min=6, message='La contraseña debe tener al menos 6 caracteres.')
        ]
    )

    confirmar_password = PasswordField(
        'Confirmar Contraseña',
        validators=[
            DataRequired(message='Confirme su contraseña.'),
            EqualTo('password', message='Las contraseñas deben coincidir.')
        ]
    )

    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    usuario = StringField(
        'Usuario',
        validators=[DataRequired(message='Ingrese su usuario.')]
    )

    password = PasswordField(
        'Contraseña',
        validators=[DataRequired(message='Ingrese su contraseña.')]
    )

    submit = SubmitField('Iniciar Sesión')
    