import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Stock Price API is Running!"

# API to fetch stock fundamentals based on user input
@app.route('/get-fundamentals', methods=['GET'])
def get_fundamentals():
    symbol = request.args.get("symbol")  # User input stock symbol

    if not symbol:
        return jsonify({"error": "Please provide a stock symbol."}), 400

    # Ensure the symbol has ".NS" only if it's not already present
    symbol = symbol.upper()
    if not symbol.endswith(".NS"):  
        symbol += ".NS"  

    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        if not info:
            return jsonify({"error": "No data found for this stock"}), 404

        data = {
            "symbol": symbol,
            "market_cap": info.get("marketCap", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "pb_ratio": info.get("priceToBook", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
        }

        return jsonify(data)

    except Exception as e:
        print("Error fetching stock fundamentals:", e)
        return jsonify({"error": "Unable to fetch data"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
