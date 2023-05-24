import imp
from datetime import datetime
import time
import statistics

readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("trader", "PROGRAM/modules/trader.py")


tsx_dict = {
    "manufacturing": ["NTR", "MG", "SAP", "STN", "DOO", "BBD-B"],
    "technology": ["SHOP", "TRI", "OTEX", "NVEI", "DSG", "GIB-A"],
    "gasoil": ["SU", "CVE", "IMO", "CNQ", "TOU", "NXE"],
    "uranium": ["CCO", "EMA", "FM"],
    "mining": ["TECK-B", "AEM", "WFG", "ABX", "FNV"],
    "banking": ["BMO", "RY", "TD", "IGM", "WN", "MFC", "BNS", "CM"],
    "retail": ["QSR", "ATD", "DOL", "TIH", "EMP-A"],
    "transportation": ["CNR", "CP", "EFN", "AC", "CCL-B", "TFII"],
}

tsx_list = [
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


goodlist = []
bad = []

tsx_list1 = ["NXE"]
run = True


def standardDeviationChecker1(reader):
    standardDeviation = statistics.stdev(reader)
    mean = statistics.mean(reader)
    z = -1.28
    zScore = (z * standardDeviation) + mean

    if standardDeviation > 1:
        return False
    else:
        return zScore


def stockFinder():
    good = ""

    for stock in tsx_list:
        finder = readerModule.StockReader(stock, "1d", "1m")
        rld = finder.regressionLineDrawer()

        standardDeviation = standardDeviationChecker1(rld[1])
        lastPrice = finder.lastPrice()

        # print(stock, lastPrice, standardDeviation)

        breakOfPattern = finder.BreakOfPattern()

        if (standardDeviation == False) or (breakOfPattern == True):
            bad.append(stock)
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

    return goodlist

    # time.sleep(60)
    # goodlist.clear()
    # bad.clear()
    # good = ""



# traderModule.Indicator(good).sendNotificationMac()
