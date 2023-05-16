import requests
import smtplib
from os import system
import time


class Indicator:
    def __init__(self, message, app="Finder"):
        self.message = message
        self.app = app

    def sendNotificationMac(self):
        system(
            f'osascript -e \'tell application "{self.app}" to display alert "{self.message}"\'&'
        )
