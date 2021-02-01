from krypto import app
from datetime import date, datetime
import sqlite3
from krypto import API

def today ():
    today = date.today ()
    today = today.strftime ("%Y-%m-%d")
    return today

def time ():
    time = datetime.now ()
    time = time.strftime ("%H:%M:%S")
    return time

def consulta (query, params=()):
    
    DBFILE = app.config ['DBFILE']

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute (query, params)
    conn.commit()
    
    filas = c.fetchall()

    conn.close()

    if len (filas) == 0:
        return filas

    columnNames = []
    for columnName in c.description:
        columnNames.append(columnName[0])

    listaDeDiccionarios = []

    for fila in filas:
        d={}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila [ix]
        listaDeDiccionarios.append (d)
    
    return listaDeDiccionarios

def coins ():
    dynamic_coins = ['EUR']

    coins = consulta('SELECT to_currency FROM movements;')

    for coin in coins:
        if coin ['to_currency'] not in dynamic_coins:
            dynamic_coins.append (coin['to_currency'])

    return dynamic_coins
            
def suma ():
    
    DBFILE = app.config ['DBFILE']

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT to_currency, to_quantity FROM movements;')
    conn.commit()

    monedas = c.fetchall()

    conn.close()

    coin_value = {}
    for key, value in monedas:
        coin_value[key] = coin_value.get(key, 0) + value

    return coin_value

def resta ():

    DBFILE = app.config ['DBFILE']

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT from_currency, from_quantity FROM movements;')
    conn.commit()

    monedas = c.fetchall()

    conn.close()

    coin_value = {}
    for key, value in monedas:
        coin_value[key] = coin_value.get(key, 0) + value

    return coin_value

def invested ():

    DBFILE = app.config ['DBFILE']

    movements = consulta ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')

    invested = 0
    for cantidad in movements:
        if cantidad ['from_currency'] == 'EUR':
            invested += cantidad ['from_quantity']
        elif cantidad ['to_currency'] == 'EUR':
            invested -= cantidad ['to_quantity']
    
    return invested

def actual_value ():

    DBFILE = app.config ['DBFILE']

    movements = consulta ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    actual_value = 0
    for cantidad in movements:
        if cantidad ['to_currency'] != 'EUR':
            Q = API.convert (cantidad ['to_quantity'], cantidad ['to_currency'], 'EUR')
            actual_value += Q
        elif cantidad ['to_currency'] == 'EUR':
            actual_value -= cantidad ['to_quantity']
        
    return actual_value
   
   

