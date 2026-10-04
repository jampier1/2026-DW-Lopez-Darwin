from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class PagoForm(FlaskForm):

    cuenta = StringField(
        "Cuenta",
        validators=[
            DataRequired(message="El número de cuenta es obligatorio."),
            Length(min=10, max=10, message="La cuenta debe tener 10 caracteres.")
        ]
    )

    concepto = StringField(
        "Concepto",
        validators=[
            DataRequired(message="El concepto es obligatorio."),
            Length(min=3, max=100, message="El concepto debe tener entre 3 y 100 caracteres.")
        ]
    )

    monto = FloatField(
        "Monto",
        validators=[
            DataRequired(message="El monto es obligatorio."),
            NumberRange(min=0.01, message="El monto debe ser mayor a 0.")
        ]
    )

    enviar = SubmitField("Registrar Pago")