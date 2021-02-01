from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
from requests import Request, Session
from krypto import app

API_KEY = app.config ['API_KEY']

def convert (Q1, C1, C2):

  if C1 != C2:

    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol={}&convert={}&CMC_PRO_API_KEY={}'

    respuesta = requests.get(url.format(C1, C2, API_KEY))

    if respuesta.status_code == 200:
        data = respuesta.json()

    Q2 = Q1 * (data ['data']['quote'][C2]['price'])

    return Q2


