from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CuentaForm(FlaskForm):

    numero = StringField(
        "Número de cuenta",
        validators=[
            DataRequired(message="El número de cuenta es obligatorio."),
            Length(
                min=10,
                max=10,
                message="El número de cuenta debe tener exactamente 10 caracteres."
            )
        ]
    )

    titular = StringField(
        "Titular",
        validators=[
            DataRequired(message="El titular es obligatorio."),
            Length(
                min=3,
                max=50,
                message="El titular debe tener entre 3 y 50 caracteres."
            )
        ]
    )

    tipo = SelectField(
        "Tipo de cuenta",
        choices=[
            ("", "Seleccione una opción"),
            ("Cuenta de Ahorros", "Cuenta de Ahorros"),
            ("Cuenta Corriente", "Cuenta Corriente")
        ],
        validators=[
            DataRequired(message="Seleccione un tipo de cuenta.")
        ]
    )

    descripcion = TextAreaField(
        "Descripción",
        validators=[
            DataRequired(message="La descripción es obligatoria."),
            Length(
                min=10,
                max=200,
                message="La descripción debe tener entre 10 y 200 caracteres."
            )
        ]
    )

    estado = SelectField(
        "Estado",
        choices=[
            ("", "Seleccione una opción"),
            ("Activa", "Activa"),
            ("Pendiente", "Pendiente")
        ],
        validators=[
            DataRequired(message="Seleccione un estado.")
        ]
    )

    enviar = SubmitField("Registrar Cuenta")