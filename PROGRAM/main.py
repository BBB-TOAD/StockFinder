import imp
from datetime import datetime
import time
import statistics

readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("trader", "PROGRAM/modules/trader.py")
regressionLineModule = imp.load_source(
    "regressionLine", "PROGRAM/modules/regressionLine.py"
)

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

tsx_list1 = regressionLineModule.stockFinder()


# for good symbols
for stocks in tsx_list1[0]:
    finder = readerModule.StockReader(stocks, "1d", "2m")
    stockCategory = finder.stockCategorization()
    print(stocks + " : " + stockCategory)
    if stockCategory == "rzone":
        pass
    elif stockCategory == "channel":
        pass
    elif stockCategory == "downTrend":
        pass

# for break of pattern symbols
