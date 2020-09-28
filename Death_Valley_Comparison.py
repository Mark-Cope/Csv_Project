import csv
from datetime import datetime

open_death= open("death_valley_2018_simple.csv", "r")
open_sitka= open("sitka_weather_2018_simple.csv", "r")


csv_d = csv.reader(open_death, delimiter= ",")
csv_s = csv.reader(open_sitka, delimiter= ",")

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
        print(f"Missing data for {current_dateD}")
    else:
        highsD.append(highD)
        lowsD.append(lowD)
        datesD.append(current_dateD)
    
for row in csv_s:
    try:
        highS = int(row[5])
        lowS = int(row[6])
        current_dateS = datetime.strptime(row[2],"%Y-%m-%d") 
        
    except ValueError:
        print(f"Missing data for {current_dateS}")
    else:
        highsS.append(highS)
        lowsS.append(lowS)
        datesS.append(current_dateS)
    

print(highsD)
print(highsS)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)


ax[0].plot(datesD, highD, c="red", alpha=0.5)
ax[0].plot(datesD, highD, c="blue", alpha=0.5)
ax[1].plot(datesS, highS, c="red", alpha=0.5)
ax[1].plot(datesS, highS, c="blue", alpha=0.5)



plt.title("Daily High and Low Temp- 2018 and Death Valley", fontsize=16)
plt.xlabel("")

plt.fill_between(datesD, highsD, lowsD, facecolor= 'blue', alpha=0.1)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)



fig.autofmt_xdate()

plt.show()