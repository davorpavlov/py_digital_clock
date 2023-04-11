import datetime as dt 
import time
import os
import locale

class Timezone:
    def __init__(self, offset_hours):
        self.offset_hours = offset_hours
        self.timezone = dt.timezone(dt.timedelta(hours=offset_hours))

    def get_time(self):
        locale.setlocale(locale.LC_ALL, 'hr_HR')
        return dt.datetime.now(self.timezone).strftime("%A %d. %B %Y. %H:%M:%S")

pacific_tz = Timezone(-7)
central_tz = Timezone(-5)
eastern_tz = Timezone(-4)

while True:
    pacific_time = pacific_tz.get_time()
    central_time = central_tz.get_time()
    eastern_time = eastern_tz.get_time()

    print("Pacific Time: ", pacific_time)
    print("Central Time: ", central_time)
    print("Eastern Time: ", eastern_time)

    time.sleep(1)
    
    os.system('cls')
