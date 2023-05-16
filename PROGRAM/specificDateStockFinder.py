import yfinance
import datetime as dt
import pandas as pd
import statistics

startdate = dt.datetime.strptime("2023-05-10 09:30:00", "%Y-%m-%d %H:%M:%S").date()
enddate = dt.datetime.strptime("2023-05-11 11:00:00", "%Y-%m-%d %H:%M:%S").date()

data = yfinance.Ticker("NVEI.TO").history(start=startdate, end=enddate, interval="1m")

companyData = pd.DataFrame.from_dict(data)

x = companyData["Close"][-1]

print(companyData)
# for i in range(386):
#     if companyData["Datetime"] == enddate:
#         print(i)

standardDeviation = statistics.stdev(companyData["Close"])
mean = statistics.mean(companyData["Close"])
z = -1.28
zScore = (z * standardDeviation) + mean

if standardDeviation > 1:
    print(False)
elif x <= standardDeviation:
    print("buy")
else:
    print("sell")
