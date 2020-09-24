import csv #Double everything with new names
from datetime import datetime

open_file= open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",")

header_row = next(csv_file)



highs = []
dates = []
lows = []



for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2],"%Y-%m-%d") 
        
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    

print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c="red", alpha= .05)
plt.plot(dates, lows, c="blue", alpha= .05)

plt.title("Daily High Temp, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", lablesize=16)

plt.fill_between(dates, highs, lows, facecolor= "blue",alpha= .01)

fig.autofmt_xdate()

plt.show()