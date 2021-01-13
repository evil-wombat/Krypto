from krypto import app
from flask import render_template, request, url_for, redirect
import sqlite3
from datetime import date, time

DBfile = 'krypto/data/database.db'


@app.route('/')
def movements_table ():
    
    conn = sqlite3.connect (DBfile)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    invested = c.fetchall()


    conn.close()
    
    return render_template ('movement_table.html', datos=invested)

@app.route ('/purchase')
def purchase ():

    return render_template ('purchase.html')


@app.route ('/status')
def status ():

    return render_template ('status.html')