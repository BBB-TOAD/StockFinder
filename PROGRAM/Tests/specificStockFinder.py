import imp
from datetime import datetime
import time

readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("trader", "PROGRAM/modules/trader.py")

tsx_list = []
run = True

while run == True:
    for stock in tsx_list:
        finder = readerModule.StockReader(stock, "1d", "1m")
        standardDeviation = finder.standardDeviationChecker()
        lastPrice = finder.lastPrice()
        # print(stock, lastPrice, standardDeviation)
        rld = finder.regressionLineDrawer()

        if standardDeviation == False:
            remove = input(
                stock
                + " has a standard deviation of "
                + standardDeviation
                + "do you wish to remove it y/n"
                + "/n"
            )
            if remove == "y":
                tsx_list.remove(stock)

        BreakOfPattern = finder.BreakOfPattern()
        if BreakOfPattern == True:
            time.sleep(30 * 60)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    time.sleep(60)

# traderModule.Indicator(good).sendNotificationMac()
