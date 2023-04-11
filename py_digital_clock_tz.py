import datetime as dt 
import time
import os
import locale
from dateutil import tz

class Timezone:
    def __init__(self, timezone_name):
        self.timezone_name = timezone_name
        self.timezone = tz.gettz(timezone_name)

    def get_time(self, locale_str: str): 
        locale.setlocale(locale.LC_ALL, locale_str)
        datetime_to_return = dt.datetime.now(self.timezone).strftime("%A %d. %B %Y. %H:%M:%S")
        locale.setlocale(locale.LC_ALL, '')
        return datetime_to_return

while True:
    timezone_name = input("Unesite vremensku zonu (npr. Europe/Zagreb): ")
    locale_str = input("Unesite lokalizaciju (npr. hr_HR za Hrvatsku): ")
    
    timezone = Timezone(timezone_name)

    while True:
        os.system('cls')
        
        current_time = timezone.get_time(locale_str)
        print(f"{timezone_name} Time: {current_time}")
        
        time.sleep(1)
