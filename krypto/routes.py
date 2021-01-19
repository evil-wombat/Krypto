from krypto import app
from flask import render_template, request, url_for, redirect
import sqlite3
from API import API

DBfile = 'krypto/data/database.db'

@app.route('/')
def movements_table ():
    
    conn = sqlite3.connect (DBfile)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    movements = c.fetchall()

    conn.close()
    
    return render_template ('movement_table.html', datos=movements)

@app.route ('/purchase', methods = ['GET', 'POST'])
def purchase ():

    if request.method == 'POST':

        conn = sqlite3.connect (DBfile)
        c = conn.cursor()

        c.execute ('INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity) VALUES (?, ?, ?, ?, ?, ?);', 
            (
                API.Date (),
                API.Time (),
                request.form.get('Coins_from'),
                request.form.get('Q_from'),
                request.form.get('Coins_to'),
                request.form.get('Q_to')
            )
        )

        conn.commit ()
        conn.close ()
    
        return redirect (url_for('movements_table'))
    
    return render_template ('purchase.html')


@app.route ('/status')
def status ():

    conn = sqlite3.connect (DBfile)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    movements = c.fetchall()

    conn.close()

    invested = 0
    for cantidad in movements:
        invested += cantidad [3]

    return render_template ('status.html', total = invested)