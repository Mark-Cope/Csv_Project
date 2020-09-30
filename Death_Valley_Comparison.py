import csv
from datetime import datetime

open_death= open("death_valley_2018_simple.csv", "r")
open_sitka= open("sitka_weather_2018_simple.csv", "r")


csv_d = csv.reader(open_death, delimiter= ",")
csv_s = csv.reader(open_sitka, delimiter= ",")

header_row = next(csv_d)
header_row = next(csv_s)

highs_D = []
dates_D = []
lows_D = []

highs_S = []
dates_S = []
lows_S = []



for row in csv_d:
    try:
        high_D = int(row[4])
        low_D = int(row[5])
        current_date_D = datetime.strptime(row[2],"%Y-%m-%d") 
        
    except ValueError:
        print(f"Missing data for {current_date_D}")
    else:
        highs_D.append(high_D)
        lows_D.append(low_D)
        dates_D.append(current_date_D)
    
for row in csv_s:
    try:
        high_S = int(row[5])
        low_S = int(row[6])
        current_date_S = datetime.strptime(row[2],"%Y-%m-%d") 
        
    except ValueError:
        print(f"Missing data for {current_date_S}")
    else:
        highs_S.append(high_S)
        lows_S.append(low_S)
        dates_S.append(current_date_S)
    



import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)


ax[0].plot(dates_D, highs_D, c="red", alpha=0.5)
ax[0].plot(dates_D, lows_D, c="blue", alpha=0.5)
ax[1].plot(dates_S, highs_S, c="red", alpha=0.5)
ax[1].plot(dates_S, lows_S, c="blue", alpha=0.5)

ax[0].set_title('Temperature comparison between SITKA Airport, AK US and Death valley, CA US\n \n SITKA AIRPORT')

plt.title('SITKA AIRPORT, AK US', fontsize=16)
plt.xlabel("", fontsize=12)

plt.title("Death Valley, CA US", fontsize=16)
plt.xlabel("", fontsize=12)

ax[1].fill_between(dates_D, highs_D, lows_D, facecolor= 'blue', alpha=0.1)
plt.tick_params(axis='both', labelsize=12)

ax[0].fill_between(dates_S, highs_S, lows_S, facecolor= 'blue', alpha=0.1)
plt.tick_params(axis='both', labelsize=12)


fig.autofmt_xdate()

plt.show()