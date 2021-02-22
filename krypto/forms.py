from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError, NumberRange


coin_list = ('EUR', 'BTC', 'ETH', 'USDT', 'DOT', 'XRP', 'ADA', 'LTC', 'BCH', 'LINK', 'XLM', 'BNB', 'USDC')

class Forms (FlaskForm):

    Coins_from = SelectField ('From', validators=[DataRequired()])
    C_from_oculto = HiddenField ()
    Q_from = FloatField ('Q', validators=[DataRequired(message='Q must be a number higher than 0.000001'), NumberRange (min=0.1, message='minimum value must be 0.1')])
    Q_from_oculto = HiddenField ()
    Coins_to = SelectField ('To', choices=coin_list, validators=[DataRequired()])
    C_to_oculto = HiddenField ()
    Q_to = FloatField ('Q')
    Q_to_oculto = HiddenField ()
    PU = FloatField ('P.U')
    PU_oculto = HiddenField ()
    

    convert = SubmitField ('Convert')
    accept = SubmitField ('Accept')
