import functions
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

ticker_id = "^FCHI"
now = dt.datetime.now().strftime("20%y-%m-%d")
ohlc = functions.get_data(ticker=ticker_id, interval="1d", start_date="2020-03-18", end_date=now)

price_close = np.flip(ohlc["Close"])
date = np.flip(ohlc["Date"])

plt.xlabel("Dates")
plt.ylabel("Close price of CAC 40")
plt.title("Evolution of CAC40 close price")
plt.plot(date, price_close)
plt.show()