from datetime import datetime
import yfinance as yf
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        now = datetime.now()
        symbol = request.form.get("symbol")
        print(symbol)
        companyInfo = yf.Ticker(symbol)
        try:
            hist = companyInfo.history(period="2d")
            if not hist.empty:
                print("chinta")
                companyName = "Adobe Systems Incorporated (ADBE)"
                twoDaysData = round(companyInfo.history(period='2d'), 2)
                yesterdayPrice = twoDaysData['Close'][0]
                todaysPrice = twoDaysData['Close'][1]
                valueChange = round(todaysPrice - yesterdayPrice, 2)
                percentChange = round((valueChange / yesterdayPrice) * 100, 2)
                tempData = {"now": now, "companyName": companyName,
                            "todaysPrice": todaysPrice, "valueChange": valueChange,
                            "percentChange": percentChange, "error": ""}
                print("sriram")
                print(tempData)
                return render_template("index.html", **tempData)
            else:
                tempData = {"error": "There is not enough data available for the requested period."}
                return render_template("index.html", **tempData)
        except:
            tempData = {"error": "You have entered wrong symbol"}
            return render_template("index.html", **tempData)

        # hist = companyInfo.history(period="2d")
        # if not hist.empty:
        #     companyName = companyInfo.info['longName']
        #     twoDaysData = round(companyInfo.history(period='2d'), 2)
        #     yesterdayPrice = twoDaysData['Close'][0]
        #     todaysPrice = twoDaysData['Close'][1]
        #     valueChange = round(todaysPrice - yesterdayPrice, 2)
        #     percentChange = round((valueChange / yesterdayPrice) * 100, 2)
        #     tempData = {"now": now, "companyName": companyName,
        #                 "todaysPrice": todaysPrice, "valueChange": valueChange,
        #                 "percentChange": percentChange, "error": ""}
        #     return render_template("index.html", **tempData)

        # else:
        #     tempData = {"error": "You have entered wrong symbol"}
        #     return render_template("index.html", **tempData)


if __name__ == '__main__':
    #app = create_app()
    app.run()
