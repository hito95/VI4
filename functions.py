import datetime as dt
import yfinance as yf
import numpy as np
import math

def get_data(ticker, interval, start_date, end_date):
    """
    Download ticker's ohlcv data for a chosen time period and time interval (either "1d", "1h", "30m", "15m", "5m")
    :param ticker       ticker id [str]
    :param interval     interval type [str]
    :param start_date   interval first day [str]
    :param end_date     interval last day [str]
    :return ohlcv       open high low close volume dataframe [df]
    """
    # Display indication
    print('[INFO] {} - Retrieving {}_{} historical data'.format(get_now(), ticker, interval))
    # Download ticker's ohlcv
    ohlcv = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    # Modify dataframe
    ohlcv.drop(columns=['Adj Close'], inplace=True)
    ohlcv.sort_index(axis=0, ascending=False, inplace=True)
    ohlcv.reset_index(inplace=True)
    if "Datetime" in ohlcv.columns:
        ohlcv['Datetime'] = ohlcv['Datetime'].astype(str).str[:-9]
    return ohlcv


def get_now():
    """
    Retrieve the current date and time
    :return:                current date and time [str]
    """
    now = dt.datetime.now()
    now_str = now.strftime("%d/%m %H:%M")
    return now_str