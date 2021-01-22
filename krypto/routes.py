from krypto import app
from flask import render_template, request, url_for, redirect
import sqlite3
from datetime import date, datetime
from krypto.forms import Forms
from krypto import API


DBFILE = app.config ['DBFILE']

@app.route('/')
def movements_table ():
    
    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    movements = c.fetchall()

    conn.close()
    
    return render_template ('movement_table.html', datos=movements)

@app.route ('/purchase', methods = ['GET', 'POST'])
def purchase ():

    form = Forms ()

    if request.method == 'POST':

        if request.form.get ('submit') == 'Acept':

            Q2 = API.convert (float (request.form.get('Q_from')), request.form.get('Coins_from'), request.form.get('Coins_to'))
            
            today = date.today ()
            today = today.strftime ("%Y-%m-%d")

            time = datetime.now ()
            time = time.strftime ("%H:%M:%S")

            conn = sqlite3.connect (DBFILE)
            c = conn.cursor()

            c.execute ('INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity) VALUES (?, ?, ?, ?, ?, ?);', 
                (
                    today,
                    time,
                    request.form.get('Coins_from'),
                    request.form.get('Q_from'),
                    request.form.get('Coins_to'),
                    round (Q2, 8)
                )
            )

            conn.commit ()
            conn.close ()
        
            return redirect (url_for('movements_table'))
        
        elif request.form.get ('submit') == 'Convert':

            Q2 = API.convert (float (request.form.get('Q_from')), request.form.get('Coins_from'), request.form.get('Coins_to'))
            PU = float (request.form.get('Q_from')) / Q2


            return render_template ('purchase.html', form = form, PU = PU, Q2=Q2)
            
            
        

    
    return render_template ('purchase.html', form = form)


@app.route ('/status')
def status ():

    conn = sqlite3.connect (DBFILE)
    c = conn.cursor()

    c.execute ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    
    movements = c.fetchall()

    conn.close()

    invested = 0
    for cantidad in movements:
        invested += cantidad [3]

    revenue = 0
    for cantidad in movements:
        Q = API.convert (cantidad [5], cantidad [4], 'EUR')
        revenue += Q


    return render_template ('status.html', total = invested, revenue = revenue)