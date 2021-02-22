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
            
def diccionario_coins_to ():
    
    DBFILE = app.config ['DBFILE']

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT to_currency, to_quantity FROM movements;')
    conn.commit()

    monedas = c.fetchall()

    conn.close()

    coins_to= {}
    for key, value in monedas:
        coins_to[key] = coins_to.get(key, 0) + value

    return coins_to

def diccionario_coins_from():

    DBFILE = app.config ['DBFILE']

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT from_currency, from_quantity FROM movements;')
    conn.commit()

    monedas = c.fetchall()

    conn.close()

    coins_from = {}
    for key, value in monedas:
        coins_from[key] = coins_from.get(key, 0) + value

    return coins_from

def total_coins_invested ():
    
    coins_to = diccionario_coins_to ()
    coins_from = diccionario_coins_from ()
    
    total = {'EUR': 0}

    for k, v in coins_to.items():

        total[k] = v - coins_from.get(k, 0)

    return total

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

    total = total_coins_invested ()

    actual_value = 0
    for k, v in total.items():
        if k != 'EUR':
            actual_value += API.convert (v, k, 'EUR')
        
    return (actual_value)
   
   

