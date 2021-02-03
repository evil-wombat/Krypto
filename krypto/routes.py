from krypto import app
from flask import render_template, request, url_for, redirect
import sqlite3
from krypto.forms import Forms
from krypto import API
from krypto import funciones

DBFILE = app.config ['DBFILE']

@app.route('/')
def movements_table ():

    messages = []

    try:    
        movements = funciones.consulta ('SELECT date, time, from_currency, from_quantity, to_currency, to_quantity FROM movements;')
    except Exception as e:
        print("**ERROR**🔧: Incorrect Database acces. {} - {}". format(type(e).__name__, e))
        messages.append("There was an error trying to access the database")

        return render_template ('movement_table.html', datos=[], messages = messages)
    
    return render_template ('movement_table.html', datos=movements, messages = messages)

@app.route ('/purchase', methods = ['GET', 'POST'])
def purchase ():

    form = Forms ()
    messages = []

    try:
        form.Coins_from.choices = funciones.coins ()
    except Exception as e:
        print("**ERROR**🔧: Incorrect Database access. {} - {}". format(type(e).__name__, e))
        messages.append("Database error.")
        return render_template ('purchase.html', form = form, fix = True, messages = messages)

    if request.method == 'POST':

        if form.validate ():

            if form.convert.data:

                try:
                    total = funciones.total_coins_invested ()
                except Exception as e:
                    print("**ERROR**🔧: Incorrect Database access. {} - {}". format(type(e).__name__, e))
                    messages.append("Database access error.")

                    return render_template ('purchase.html', form = form, fix = True, messages = messages)

                if (form.Coins_from.data == 'EUR' and form.Coins_from.data != form.Coins_to.data) or (form.Q_from.data < total [form.Coins_from.data]):

                    try:
                        form.Q_to.data = API.convert (float (form.Q_from.data), form.Coins_from.data, form.Coins_to.data)
                    except Exception as e:
                        print("**ERROR**🔧: Incorrect API access. {} - {}". format(type(e).__name__, e))
                        messages.append("API_KEY error")

                        return render_template ('purchase.html', form = form, fix = True, messages = messages)
                    
                    form.PU.data = float (form.Q_from.data) / form.Q_to.data

                    form.Q_to_oculto.data = form.Q_to.data
                    form.PU_oculto.data = form.PU.data
                    form.C_from_oculto.data = form.Coins_from.data  
                    form.C_to_oculto.data = form.Coins_to.data 
                    form.Q_from_oculto.data = form.Q_from.data 
                    
                    return render_template ('purchase.html', form = form, fix = True, messages = messages)

                else:
                    if form.Coins_from.data == form.Coins_to.data:

                        messages.append ('You are trying to exchange the same Coin!!')
                        return render_template ('purchase.html', form = form, messages = messages)
                    
                    elif form.Q_from.data > total [form.Coins_from.data]:

                        messages.append ('You do not have enough coins!!')
                        return render_template ('purchase.html', form = form, messages = messages)
                    
                return render_template ('purchase.html', form = form)                    
          
            elif form.accept.data: 

                try:
                    funciones.consulta ('INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity) VALUES (?, ?, ?, ?, ?, ?);', 
                        (
                            funciones.today (), funciones.time (),
                            form.C_from_oculto.data,
                            form.Q_from_oculto.data,
                            form.C_to_oculto.data,
                            form.Q_to_oculto.data
                        )
                    )
                except Exception as e:
                    print("**ERROR**🔧: Incorrect Database acces. {} - {}". format(type(e).__name__, e))
                    messages.append("There was an error trying to access the database")

                    return render_template ('purchase.html', form = form, fix = True, messages = messages)
            
                return redirect (url_for('movements_table'))
        
        return render_template ('purchase.html', form = form, messages=messages)

    return render_template ('purchase.html', form = form)


@app.route ('/status')
def status ():
    messages = []

    try:
        invested = funciones.invested()
    except Exception as e:
        print("**ERROR**🔧: Incorrect Database acces. {} - {}". format(type(e).__name__, e))
        messages.append("There was an error trying to access the database")
        return render_template ('status.html', total = (), actual_value = (), messages = messages)

    try:
        actual_value = funciones.actual_value ()
    except Exception as e:
        print("**ERROR**🔧: Incorrect API access. {} - {}". format(type(e).__name__, e))
        messages.append("API_KEY error")

        return render_template ('status.html', total = (), actual_value = (), messages = messages)
    

    return render_template ('status.html', total = invested, actual_value = actual_value)

    