import time
import imp

# Run every 10 minsx


readerModule = imp.load_source("reader", "PROGRAM/modules/reader.py")

stock = ["AEM"]
bought = False


if __name__ == "__main__":
    while True:
        time.sleep(60)

        if bought == True:
            finder = readerModule.StockReader(stock, "1d", "1m")
            sell = finder.lastTwoDifferencesInPrice()
            if sell == False:
                print("Hold")
            else:
                print("Sell")


# from wsimple.api import Wsimple


# def get_otp():
#     return input("Enter otpnumber: \n>>>")


# email = str(input("Enter email: \n>>>"))
# password = str(input("Enter password: \n>>>"))
# stock = "NXE.TO"
# stockAmount = 1000

# ws = Wsimple(email, password, otp_callback=get_otp)

# # always check if wealthsimple is working (return True if working or an error)
# if ws.is_operational():
#     # check the current operation status of internal Wealthsimple Trade
#     print(ws.current_status())
#     # Make a Market Order
#     ws.market_buy_order(stock, stockAmount)
#     # Make a Market Sell
#     ws.market_sell_order(stock, stockAmount)
