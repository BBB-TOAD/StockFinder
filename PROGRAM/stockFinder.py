import imp
from datetime import datetime

readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")
traderModule = imp.load_source("trader", "PROGRAM/modules/trader.py")


tsx_dict = {
    "manufacturing": ["NTR", "MG", "SAP", "STN", "DOO", "BBD-B"],
    "technology": ["SHOP", "TRI", "OTEX", "NVEI", "DSG", "GIB-A"],
    "gasoil": ["SU", "CVE", "IMO", "CNQ", "TOU"],
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
good = ""

for stock in tsx_list:
    finder = readerModule.StockReader(stock, "1d", "1m")
    standardDeviation = finder.standardDeviationChecker()
    lastPrice = finder.lastPrice()
    if standardDeviation == False:
        bad.append(stock)
    elif lastPrice <= standardDeviation:
        goodlist.append(stock)
    else:
        bad.append(stock)
    print(lastPrice, standardDeviation)


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

for stock in goodlist:
    good += str(stock)


traderModule.Indicator(good).sendNotificationMac()
