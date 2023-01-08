from yahoo_fin.stock_info import *            #pip install yahoo-fin and pands and requests-html


stock = input("Please enter a ticker symbol")

if stock.upper in tickers_sp500():
    print("The stock is the S&P 500")

else:
    print("Not in the S&P 500")    
