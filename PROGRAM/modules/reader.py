import yfinance as yf
import pandas as pd
import statistics

# Calculate the standard deviation from a sample of data


class StockReader:
    def __init__(self, stockSymbol, period, interval, index=".TO"):
        self.stockSymbol = stockSymbol
        self.period = period
        self.interval = interval
        self.index = index

    def findData(self):
        i = yf.Ticker(self.stockSymbol + self.index).history(
            period=self.period, interval=self.interval
        )
        return i

    def reader(self):
        companyData = pd.DataFrame.from_dict(self.findData())
        return companyData

    def lastPrice(self):
        x = self.reader()["Close"][-1]

        return x

    def lastTwoOpenPrices(self):
        x = self.reader()["Open"][-2:]

        return x

    def lastTwoClosePrices(self):
        x = self.reader()["Close"][-2:]
        return x

    def lastTwoDifferencesInPrice(self):
        LTO = self.lastTwoOpenPrices()
        LTC = self.lastTwoClosePrices()
        FD = LTO[0] - LTC[0]
        SD = LTO[1] - LTC[1]

        if FD < 0 and SD < 0:
            return True
        else:
            return False

    # Pattern Checker Functions

    def standardDeviationChecker(self):
        reader = self.reader()
        standardDeviation = statistics.stdev(reader["Close"])
        mean = statistics.mean(reader["Close"])
        z = -1.28
        zScore = (z * standardDeviation) + mean

        if standardDeviation > 1:
            return False
        else:
            return zScore
