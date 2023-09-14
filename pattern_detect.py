import talib
import yfinance as yf   

data = yf.download("SPY", start="2023-01-01", end="2023-05-20")
#print(data)

morning_stars = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
data['Morning Star'] = morning_stars
data['Engulfing'] = engulfing

#print (data)

engulfing_day = data[data['Engulfing'] != 0]

print(engulfing_day) 