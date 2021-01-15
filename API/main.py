from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def API_Name (param):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'12',
    'convert':'EUR'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4db76d23-bbcf-4e27-87b0-146f16084535',
  }

  session = Session()
  session.headers.update(headers)
  
  list_params = []

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    
    for i in range (0, 12):
      a = (data['data'][i][param])
      list_params.append (a)
    
    return (list_params)
    
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
  


def API_Price (param):
  
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'12',
    'convert':'EUR'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4db76d23-bbcf-4e27-87b0-146f16084535',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    
    for i in range (0, 12):
      return(data ['data'][i][param]['EUR']['price'])

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

symbols = API_Name ('symbol')
print (symbols [0])