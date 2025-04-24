import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'

# Read death valley file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Read Sitka file
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)

    # Get dates, and high and low temperatures from this file.
    dates2, highs2, lows2 = [], [], []
    for row2 in reader2:
        current_date2 = datetime.strptime(row2[2], '%Y-%m-%d')
        try:
            high2 = int(row2[5])
            low2 = int(row2[6])
        except ValueError:
            print(f"Missing data for {current_date2}.")
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates2, highs2, c='green', alpha=0.5)
ax.plot(dates2, lows2, c='yellow', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.fill_between(dates2, highs2, lows2, facecolor='yellow', alpha=0.1)


# Format plot.
title = "Daily high and low temperatures - 2018\nSitka and Death Valley Comp."
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()