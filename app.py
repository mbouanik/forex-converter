from flask import Flask, render_template, request, redirect, flash
import requests
from currency_symbols import CurrencySymbols

app = Flask(__name__)
app.config["SECRET_KEY"] = "lkfj324234lkhkhs0a"


@app.route("/")
def home():
    return render_template("app.html")


@app.route("/converter", methods=["POST"])
def converter():
    curency_one = request.form.get("currency_one").upper()
    currency_two = request.form.get("currency_two").upper()
    amount = request.form.get("amount", 1)

    symbols_response = requests.get("https://api.exchangerate.host/symbols")
    symbols = symbols_response.json()["symbols"]

    if curency_one not in symbols:
        flash(f"Not a valid currency {curency_one}", "error")
    elif currency_two not in symbols:
        flash(f"Not a valid currency {currency_two}", "error")
    else:
        url = f"https://api.exchangerate.host/convert"
        response = requests.get(
            url,
            params={
                "from": curency_one,
                "to": currency_two,
                "amount": amount,
                "places": 2,
                "symbols": currency_two,
            },
        )
        data = response.json()
        print(data)
        return render_template(
            "converter.html",
            currency=f"{CurrencySymbols.get_symbol(currency_two)} {data['result']}",
        )
    return render_template("app.html")


if __name__ == "__main__":
    app.run(debug=True)
