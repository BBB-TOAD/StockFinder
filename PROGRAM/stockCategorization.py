import imp
from datetime import datetime
import time
import statistics

readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("trader", "PROGRAM/modules/trader.py")
stockFinderModule = imp.load_source("stockFinder", "PROGRAM/stockFinder.py")

tsx_list = stockFinderModule.stockFinder()

for stocks in tsx_list:
    finder = readerModule.StockReader(stocks, "1d", "1m")
    stockCategory = finder.stockCategorization()
    print(stockCategory)
    if stockCategory == "rzone":
        print("rzone")
    elif stockCategory == "channel":
        print("channel")
    elif stockCategory == "downTrend":
        print("downTrend")
