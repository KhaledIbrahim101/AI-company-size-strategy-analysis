# yahoo_finance_parser.py
import yfinance as yf
import pandas as pd

def fetch_yahoo_financials(company_tickers):
    results = []

    for name, ticker in company_tickers.items():
        try:
            print(f"Fetching {name} ({ticker})...")
            stock = yf.Ticker(ticker)
            info = stock.info

            data = {
                "Company": name,
                "Ticker": ticker,
                "MarketCap": info.get("marketCap", None) / 1e9 if info.get("marketCap") else None,
                "Revenue": info.get("totalRevenue", None) / 1e9 if info.get("totalRevenue") else None,
                "Employees": info.get("fullTimeEmployees", None),
                "PE_Ratio": info.get("trailingPE", None),
                "Forward_EPS": info.get("forwardEps", None),
                "Trailing_EPS": info.get("trailingEps", None),
                "Beta": info.get("beta", None),
                "DividendYield": info.get("dividendYield", None),
                "Sector": info.get("sector", None),
                "Industry": info.get("industry", None)
            }

            results.append(data)
        except Exception as e:
            print(f"⚠️ Error fetching data for {name}: {e}")

    df = pd.DataFrame(results)
    df.to_csv("yahoo_finance_data.csv", index=False)
    print("✅ Yahoo Finance data saved to yahoo_finance_data.csv")

# Example usage:
# company_tickers = {
#     "Microsoft": "MSFT",
#     "Apple": "AAPL",
#     "Google": "GOOGL"
# }
# fetch_yahoo_financials(company_tickers)
