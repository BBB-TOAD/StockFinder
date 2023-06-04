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
rlmodule = imp.load_source("regressionLine", "PROGRAM/modules/regressionLine.py")


class QualityControlSystem:
    def __init__(self, categoryType):
        self.categoryType = categoryType

    def categoryTypeFunction(self):
        if self.categoryType == "rzone":
            rzone = self.rzoneChecker()
            if rzone == "low":
                zscore = -1.28
            elif rzone == "high":
                zscore = 1.3
        elif self.categoryType == "channel":
            channel = self.channelChecker()
            if channel == "low":
                zscore = -0.67
            elif channel == "high":
                zscore = 0.68
        return zscore

    def rzoneChecker(self):
        pass

    def channelChecker(self):
        pass
