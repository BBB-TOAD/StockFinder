import requests
import smtplib
import time

api_key = "asdfadsf adsf af"
password = "tesasdfdsafads"


def send_mail(password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("codingandfun@gmail.com", password)
    subject = "test"
    body = "price down"

    msg = f"subject: {subject} {body}"

    server.sendmail("codingandfun@gmail.com", "codingandfun@gmail.com", msg)
    print("email is sent")
    server.quit()


def price_tracker(api_key, password):
    prices = requests.get(
        f"https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key}"
    ).json()
    stockPrice = prices[0]["price"]
    print(stockPrice)
    if stockPrice < 140:
        send_mail(password)


# run evrey 10 minutes
while True:
    price_tracker(api_key, password)
    time.sleep(600)
