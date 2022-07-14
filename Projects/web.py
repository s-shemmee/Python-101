from flask import Flask, render_template
from googlefinance import getQuotes
app = Flask(__name__)

def get_stock_price(ticker):
    return f"{ticker} is trading at ${getQuotes(ticker)[0]['LastTradePrice']}"

@app.route("/")
def index():
    greeting = "Hello from One Month Python!"
    return render_template("index.html", greeting=greeting)

@app.route("/<ticker>")
def stock_price(ticker):
    price = get_stock_price(ticker)
    return render_template("stock_price.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)