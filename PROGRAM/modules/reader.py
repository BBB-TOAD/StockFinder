import yfinance as yf
import pandas as pd
import statistics
import statsmodels.formula.api as sm
from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = formula
    plt.plot(x, y)
    plt.show()


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

    def regressionLineDrawer(self):
        reader = self.reader()
        Closelist = reader["Close"]

        numberslist = numberlist(len(Closelist))
        lineregress = linregress(numberslist, Closelist)

        A = lineregress.intercept
        B = lineregress.slope

        x = Closelist
        xvalues = numberlist(len(x))

        ylist = []

        for xamnt in x:
            sdy = statistics.stdev(x)
            sdx = statistics.stdev(xvalues)
            meany = statistics.mean(Closelist)
            meanx = statistics.mean(xvalues)
            r = np.corrcoef(xvalues, x)

            B = r[0, 1] * (sdy / sdx)
            A = meany - B * meanx
            yhat = A + B * xamnt
            ylist.append(yhat)

        returnValues = []
        returnValues.append(x)
        returnValues.append(ylist)

        return returnValues

        # print(x, ylist)

        # Create the plot
        # plt.plot(range(len(x)), ylist)

        # # Show the plot
        # plt.show()

        # result = sm.ols(formula="Y ~ A + B", data=reader).fit()
        # return result.params

    # Bullish Cathegorization Algorithms
    def stockCategorization(self):
        regressionLineDrawer = self.regressionLineDrawer()

        lengthX = numberlist(len(regressionLineDrawer[0]))

        lineregressCategorization = linregress(lengthX, regressionLineDrawer[1])
        slopeCategorization = lineregressCategorization.slope

        # print("slope Cat :   " + slopeCategorization)

        if 0 < slopeCategorization < 0.2:
            rzone = "rzone"
            return rzone
        elif slopeCategorization > 0.2:
            channel = "channel"
            return channel
        elif slopeCategorization < 0:
            downTrend = "downTrend"
            return downTrend

    # Bearish Cathegorization Algorithms

    def BreakOfPattern(self):
        priceChange = 0.04
        reader = self.reader()
        closeList = reader["Close"]

        beforeInterval = int(closeList[-4])
        afterInterval = int(closeList[-1])

        plusChange = (beforeInterval * priceChange) + beforeInterval
        minusChange = beforeInterval - (beforeInterval * priceChange)

        if (afterInterval < minusChange) or (afterInterval > plusChange):
            return True
        else:
            return False


# slope=0.0004538262435010833, intercept=83.5472103148518, rvalue=0.22948935470084256, pvalue=4.949317011784705e-06, stderr=9.796819741961173e-05, intercept_stderr=0.021903616440809046


def numberlist(number):
    numberlist = []
    for numbers in range(int(number)):
        numberlist.append(numbers)
    return numberlist
