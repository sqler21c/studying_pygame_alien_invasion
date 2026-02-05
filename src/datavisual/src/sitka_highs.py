from pathlib import Path
import csv
from find_dir import find_dir

import matplotlib.pyplot as plt
from datetime import datetime

path_file = find_dir(1,"weather_data","sitka_weather_2021_simple.csv")


path = Path(path_file)
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# print(header_row)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# 날짜와 최고, 최저 기온을 추출
dates, highs, lows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    
    high = int(row[4])
    highs.append(high)

    low = int(row[5])
    lows.append(low)

# print(highs)

# 최고 기온을 그래프로 그림
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format graph
ax.set_title("Daily high & low temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()