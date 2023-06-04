import yfinance as yf
import pandas as pd
import statistics
import statsmodels.formula.api as sm
from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import imp
import datetime

stockFinderModule = imp.load_source("StockReader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("Indicator", "PROGRAM/modules/trader.py")

numberlist = stockFinderModule.numberlist()


class RegressionLine(stockFinderModule.StockReader):
    def __init__(self, stockSymbol, period, interval, index):
        super().__init__(stockSymbol, period, interval, index)

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

        if 0 < slopeCategorization < 0.000001:
            rzone = "rzone"
            return rzone
        elif slopeCategorization > 0.000001:
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

def stockFinder():
    # String for good list
    good = ""

    # good list
    goodlist = []

    # bad list
    bad = []

    # Thirty minute watch for break of pattern
    ThirtyMinutes = []

    # List to return
    returnList = []

    for stock in tsx_list1:
        finder = stockFinderModule.StockReader(stock, "1d", "1m")
        rld = finder.regressionLineDrawer()

        standardDeviation = standardDeviationChecker1(rld[1])
        lastPrice = finder.lastPrice()

        # print(stock, lastPrice, standardDeviation)

        breakOfPattern = finder.BreakOfPattern()

        if standardDeviation == False:
            bad.append(stock)
        elif breakOfPattern == True:
            ThirtyMinutes.append(stock)
        elif lastPrice <= standardDeviation:
            goodlist.append(stock)
        else:
            bad.append(stock)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    for stock in goodlist:
        good += str(stock) + " "

    print(good)

    returnList.append(goodlist)
    returnList.append(ThirtyMinutes)

    return returnList



tsx_list1 = [
    "NTR",
    "MG",
    "SAP",
    "STN",
    "DOO",
    "BBD-B",
    "SHOP",
    "TRI",
    "OTEX",
    "NXE",
    "NVEI",
    "DSG",
    "GIB-A",
    "SU",
    "CVE",
    "IMO",
    "CNQ",
    "TOU",
    "CCO",
    "EMA",
    "FM",
    "TECK-B",
    "AEM",
    "WFG",
    "ABX",
    "FNV",
    "BMO",
    "RY",
    "TD",
    "IGM",
    "WN",
    "MFC",
    "BNS",
    "CM",
    "QSR",
    "ATD",
    "DOL",
    "TIH",
    "EMP-A",
    "CNR",
    "CP",
    "EFN",
    "AC",
    "CCL-B",
    "TFII",
]

def standardDeviationChecker1(readable):
    standardDeviation = statistics.stdev(readable)
    mean = statistics.mean(readable)
    z = -1.28
    zScore = (z * standardDeviation) + mean

    if standardDeviation > 1:
        return False
    else:
        return zScore


# slope=0.0004538262435010833, intercept=83.5472103148518, rvalue=0.22948935470084256, pvalue=4.949317011784705e-06, stderr=9.796819741961173e-05, intercept_stderr=0.021903616440809046
