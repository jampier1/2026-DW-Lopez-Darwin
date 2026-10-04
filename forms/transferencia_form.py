from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class TransferenciaForm(FlaskForm):

    tipo = StringField(
        "Tipo de transferencia",
        validators=[
            DataRequired(message="El tipo de transferencia es obligatorio."),
            Length(min=5, max=50, message="Debe tener entre 5 y 50 caracteres.")
        ]
    )

    origen = StringField(
        "Cuenta origen",
        validators=[
            DataRequired(message="La cuenta de origen es obligatoria."),
            Length(min=10, max=10, message="La cuenta debe tener 10 caracteres.")
        ]
    )

    destino = StringField(
        "Cuenta destino",
        validators=[
            DataRequired(message="La cuenta de destino es obligatoria."),
            Length(min=10, max=10, message="La cuenta debe tener 10 caracteres.")
        ]
    )

    monto = FloatField(
        "Monto",
        validators=[
            DataRequired(message="El monto es obligatorio."),
            NumberRange(min=0.01, message="El monto debe ser mayor a 0.")
        ]
    )

    enviar = SubmitField("Registrar Transferencia")