import csv
from datetime import datetime

open_death= open("death_valley_2018_simple.csv", "r")
open_sitka= open("sitka_weather_2018_simple.csv", "r")


csv_d = csv.reader(open_file, delimiter= ",")
csv_s = csv.reader(open_file, delimiter= ",")

header_row = next(csv_d)
header_row = next(csv_s)

highsD = []
datesD = []
lowsD = []

highsS = []
datesS = []
lowsS = []



for row in csv_d:
    try:
        highD = int(row[4])
        lowD = int(row[5])
        current_dateD = datetime.strptime(row[2],"%Y-%m-%d") 
        
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highsD.append(highD)
        lowsD.append(lowD)
        datesD.append(current_dateD)
    

print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c="red", alpha= 0.5)
plt.plot(dates, lows, c="blue", alpha= 0.5)

plt.title("Daily High Temp, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.fill_between(dates, highs, lows, facecolor= "blue",alpha= 0.1)

fig.autofmt_xdate()

plt.show()