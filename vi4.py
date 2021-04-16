import functions
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random

ticker_id = "GLE.PA"
now = dt.datetime.now().strftime("20%y-%m-%d")
ohlc = functions.get_data(ticker=ticker_id, interval="1d", start_date="2020-03-18", end_date=now)

price_close = list(np.flip(ohlc["Close"]))
date = list(np.flip(ohlc["Date"]))

plt.xlabel("Dates")
plt.ylabel("Close price of CAC 40")
plt.title("Evolution of CAC40 close price")
plt.plot(date, price_close)
plt.show()


""" ------------------------------------------------- TEST ------------------------------------------------- """

liste_ticker = ["VIV.PA","EN.PA","SAN.PA","ENGI.PA","AI.PA","ORA.PA","BN.PA","WLN.PA","BNP.PA","SGO.PA","MC.PA","LR.PA","ACA.PA","RI.PA","SW.PA","SU.PA","OR.PA","CA.PA","ML.PA","GLE.PA","AC.PA","FP.PA","KER.PA","CAP.PA","VIE.PA","DG.PA","HO.PA","AIR.PA","ATO.PA"]

date = []
price_close = []
n = len(liste_ticker)


for i in range(n):
    now = dt.datetime.now().strftime("20%y-%m-%d")
    ohlc = functions.get_data(ticker=liste_ticker[i], interval="1d", start_date="2016-03-18", end_date=now)
    price_close.append(list(np.flip(ohlc["Close"])))

date = list(np.flip(ohlc["Date"]))


plt.figure("Figure 1")
plt.xlabel("Dates")
plt.ylabel("Close price ")
plt.title("Evolution of close price")
for i in range(n):
    plt.plot(date, price_close[i])
plt.show()

yields = []

for i in range(n):
    tempo = np.zeros(len(price_close[i]))
    tempo = list(tempo)
    for j in range(1, len(price_close[i])):
        tempo[j] = (price_close[i][j] - price_close[i][j - 1]) / price_close[i][j - 1]
    yields.append(tempo)


def random_weight(n):
    return np.random.random(n)

weight = random_weight(n)

var = []
    
for i in range(n):
    var.append(np.var(yields[i]))
    
covar = np.cov(yields)

n = len(yields)
    
mean = []
for i in range(n):
    mean.append(np.mean(yields[i]))



def mean_portfolio(weight):
    return np.mean(mean)


def var_portfolio(weight):    
    sum_ = 0
    for i in range(n):
        sum_2 = 0
        for j in range(n):
            sum_2 += weight[i]*weight[j]*covar[i,j]
        sum_ += var[i]*weight[i]**2 + 2*sum_2
    
    return sum_
        

var_port = var_portfolio(weight)


def contraint1(weight):
    return sum(weight) - 1

mu = 0
mu_max = max(mean)

def contraint2(weight):
    return mean_portfolio(weight) - mu

cons = [{'type':'eq', 'fun': contraint1},
        {'type':'ineq', 'fun': contraint2}]

non_neg = []
for i in range(n):
    non_neg.append((0,None))
non_neg = tuple(non_neg)

volatility_curve = []
returns_curve = []

nb_point = 10

for i in range(nb_point):
    mu = mu_max*i/nb_point
    markowitz_limit = minimize(fun = var_portfolio, x0 = weight, method='SLSQP', constraints=cons, bounds = non_neg )
    returns_curve.append(mean_portfolio(markowitz_limit.x))
    volatility_curve.append(np.sqrt(markowitz_limit.fun))
    print("{}%".format(i*100/nb_point))
    
plt.figure("Figure 2")
plt.xlabel("Standard deviation")
plt.ylabel("Returns")
plt.title("Efficient limit")
plt.plot(volatility_curve, returns_curve)