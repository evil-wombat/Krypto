from krypto import app
from flask import render_template




@app.route('/')
def movements_table ():

    return render_template ('movement_table.html')

@app.route ('/purchase')
def purchase ():

    return render_template ('purchase.html')


@app.route ('/status')
def status ():

    return render_template ('status.html')