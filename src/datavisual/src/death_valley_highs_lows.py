from pathlib import Path
import csv

from find_dir import find_dir as fd

import matplotlib.pyplot as plt
from datetime import datetime


path_low = fd(1, 'weather_data', 'death_valley_2021_simple.csv')
path = Path(path_low)
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

dates, highs, lows = [], [], []

for row in reader:
    curent_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {curent_date}")
    else:
        dates.append(curent_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily high & low temperatures - Death Valley, 2021"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
