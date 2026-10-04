from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SolicitudForm(FlaskForm):

    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=50, message="El nombre debe tener entre 3 y 50 caracteres.")
        ]
    )

    correo = StringField(
        "Correo Electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingrese un correo electrónico válido.")
        ]
    )

    tipo_solicitud = SelectField(
        "Tipo de Solicitud",
        choices=[
            ("", "Seleccione una opción"),
            ("Apertura de cuenta", "Apertura de cuenta"),
            ("Transferencia", "Transferencia"),
            ("Retiro de dinero", "Retiro de dinero"),
            ("Consulta de saldo", "Consulta de saldo")
        ],
        validators=[
            DataRequired(message="Seleccione un tipo de solicitud.")
        ]
    )

    asunto = StringField(
        "Asunto",
        validators=[
            DataRequired(message="El asunto es obligatorio."),
            Length(min=3, max=100, message="El asunto debe tener entre 3 y 100 caracteres.")
        ]
    )

    mensaje = TextAreaField(
        "Mensaje",
        validators=[
            DataRequired(message="El mensaje es obligatorio."),
            Length(min=10, max=500, message="El mensaje debe tener entre 10 y 500 caracteres.")
        ]
    )

    enviar = SubmitField("Enviar Solicitud")