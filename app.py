import os, csv
import talib
import yfinance as yf
import pandas as pd
from flask import Flask, escape, request, render_template
from patterns import patterns

app = Flask(__name__)

@app.route('/snapshot')
def snapshot():
    with open('datasets/cryptos.csv') as f:

        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
    #        print(symbol)
            data = yf.download(symbol, start="2023-01-01", end=None)
            data.to_csv('datasets/daily/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

@app.route('/')
def index():
   
    pattern  = request.args.get('pattern', None)
    stocks = {}
    with open('datasets/cryptos.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}
    #print(stocks)   
    if pattern:
        
        datafiles = os.listdir('datasets/daily')
        for filename in datafiles:
           df = pd.read_csv('datasets/daily/{}'.format(filename))
           
           pattern_function = getattr(talib, pattern)
           symbol = filename.split('.')[0]
           try:      
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                #
                last = results.tail(1).values[0]
                #print(last)
                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:  
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None                   
            
           except:
               pass 
            
    
    return render_template('index.html', patterns=patterns, stocks=stocks, current_pattern=pattern)
