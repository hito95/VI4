import functions
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

ticker_id = "^FCHI"
now = dt.datetime.now().strftime("20%y-%m-%d")
ohlc = functions.get_data(ticker=ticker_id, interval="1d", start_date="2020-03-18", end_date=now)

price = np.flip(ohlc["Close"])
date = np.flip(ohlc["Date"])

plt.plot(date, price)