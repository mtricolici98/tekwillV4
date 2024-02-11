from flask import Flask, request

from classwork_24.homework_currency_converter import ConversionFileService, CurrencyConversionService

app = Flask(__name__)


@app.route("/")
def hello_world():
    for header, value in request.headers.items():
        print(header, value)
    return "<h1>Hello World!</h1>"


@app.route("/convert/<currency>/<amount>/")
def convert(currency, amount):
    try:
        amount = float(amount)
    except ValueError:
        return f"<h1>Invalid value \"{amount}\" to convert</h1>"
    conversion_data = ConversionFileService.load_from_url('MDL', 'https://www.floatrates.com/daily/mdl.json')
    converter = CurrencyConversionService(conversion_data)
    try:
        amount_in_eur = converter.convert("MDL", currency, amount)
    except ValueError:
        return f"<h1>Conversion to {currency} not possible</h1>"
    return f"<h1>{amount} mdl is {amount_in_eur:.2f} {currency}</h1>"


app.run(debug=True)
