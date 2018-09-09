#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

content = open('body-comp.csv', 'r')

dates = []
weight = []
bf = []
goal = []
for i, line in enumerate(content):
    line = line.split(',')
    if i==0:
        labels = line
        continue
    dates.append(mdates.date2num(datetime.strptime(line[0], '%m/%d/%y').date()))
    weight.append(float(line[1]))
    bf.append(float(line[2]))
    goal.append(line[3])


print(dates)
print(weight)
print(bf)

fig, ax1 = plt.subplots()
ax1.plot_date(dates, weight, '.k')
ax1.set_xlabel('Date')
ax1.set_ylabel('Weight [lbs]')

ax2 = ax1.twinx()
ax2.plot_date(dates, bf, '*r')
ax2.set_ylabel('BF [%]')
plt.xticks(dates, rotation='vertical')
plt.show()
