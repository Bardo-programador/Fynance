import yfinance as yf
import os
situacao = False
def verificaPasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)


tickers =['FNF', 'ASML', 'GOOGL', 'AAPL']

verificaPasta("dados")


for ticker in tickers:
    data = yf.download(ticker, group_by="ticker", period='20y')
    data.to_csv(f"dados/{ticker}.csv")
    if os.path.exists(f"dados/{ticker}.csv"):
        print("Ticker: "+ticker+" baixado")
    else:
        print("Arquivo não baixado")

situacao = True