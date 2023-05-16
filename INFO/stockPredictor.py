import yfinance as yf
import pandas as pd
import statistics

# Calculate the standard deviation from a sample of data


i = yf.Ticker("NXE.TO").history(period="1d", interval="1m")

companyData = pd.DataFrame.from_dict(i)

standardDeviation = statistics.stdev(companyData["Close"])
mean = statistics.mean(companyData["Close"])
z = -1.28
zScore = (z * standardDeviation) + mean

x = companyData["Close"][-1]
print(x)

print(zScore)

if x <= zScore:
    print("buy")
else:
    print("sell")
