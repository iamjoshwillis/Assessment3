from flask import Flask, request, render_template
from forex_python.converter import CurrencyCodes
import requests
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "2468"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def convert():
    try:
        starting = request.form["from"].upper()
        ending = request.form["to"].upper()
        amount = request.form["amount"]

        response = requests.post(f'http://api.exchangerate.host/convert?access_key=d7a2c7016fb2ed66a9cf4d3bd9e3e1f9&from={starting}&to={ending}&amount={amount}')
        converted = response.json()['result']
        rounded_conversion = round(converted, 2)

        symbol = CurrencyCodes()
        ending_symbol = symbol.get_symbol(ending)
        
        return f'<h1>Converted Amount: {ending_symbol}{rounded_conversion}'
    
    except: print("Please fix invalid parameter")