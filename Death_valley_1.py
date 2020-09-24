import csv
from datetime import datetime

open_file= open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",")

header_row = next(csv_file)
'''
print(header_row)

for index, column_header in enumerate (header_row):
    print(index,column_header)
'''
highs = []
dates = []
lows = []
'''
x = datetime.strptime('2018-07-01', "%Y-%m-%d")
print(x)
'''


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


plt.plot(dates, highs, c="red", alpha= 0.5)
plt.plot(dates, lows, c="blue", alpha= 0.5)

plt.title("Daily High Temp, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.fill_between(dates, highs, lows, facecolor= "blue",alpha= 0.1)

fig.autofmt_xdate()

plt.show()