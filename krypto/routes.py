from krypto import app
from flask import render_template, request, url_for, redirect
import sqlite3
from datetime import date, time
from API import main

DBfile = 'krypto/data/database.db'


@app.route('/')
def movements_table ():
    
    conn = sqlite3.connect (DBfile)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    movements = c.fetchall()

    conn.close()
    
    return render_template ('movement_table.html', datos=movements)

@app.route ('/purchase')
def purchase ():

    symbols = main.API_Name ('symbol')

    return render_template ('purchase.html', symbols = symbols)


@app.route ('/status')
def status ():

    return render_template ('status.html')