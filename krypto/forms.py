from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired


coin_list = ('EUR', 'BTC', 'ETH', 'USDT', 'DOT', 'XRP', 'ADA', 'LTC', 'BCH', 'LINK', 'XLM', 'BNB', 'USDC')

class Forms (FlaskForm):

    Coins_from = SelectField ('From', choices=coin_list)
    Q_from = FloatField ('Q', validators=[DataRequired()])
    Coins_to = SelectField ('To', choices=coin_list)
    Q_to = FloatField ('Q')
    PU = FloatField ('P.U.')
