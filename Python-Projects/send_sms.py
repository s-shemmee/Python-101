from twilio.rest import Client
from googlefinance import getQuotes

def get_stock_price(ticker):
    return f"{ticker} is trading at ${getQuotes(ticker)[0]['LastTradePrice']}"

def send_text(message):
    account = "AC9c5237acf6f9474baff618edcc116939"
    token = "24805c5150cdaf85727269c24617b1cf"
    client = Client(account, token)

    message = client.messages.create(to="+12016473233", from_="+16464900357",
                                 body=message)

stocks = ["AAPL", "GOOG", "FB"]

for stock in stocks:
    send_text(get_stock_price(stock))