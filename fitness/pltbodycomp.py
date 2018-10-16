#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filter", help="You can choose to reduce noise of data", action='store_true')
parser.add_argument("--type", help="Define either 'bulk' or 'cut'")
args = parser.parse_args()

content = open('body-comp.csv', 'r')

dates = []
weight = []
bf = []
goal = []
for i, line in enumerate(content):
    line = line.split(',')
    if i==0 or not line[1] or args.type.lower() not in line[3].lower():
        labels = line
        continue
    dates.append(mdates.date2num(datetime.strptime(line[0], '%m/%d/%y').date()))
    weight.append(float(line[1]))
    bf.append(float(line[2]))
    goal.append(line[3])

fig, ax1 = plt.subplots()
ax1.plot_date(dates, weight, 'k', label="Weight")
ax1.set_xlabel('Date')
ax1.set_ylabel('Weight [lbs]')

ax2 = ax1.twinx()
ax2.plot_date(dates, bf, 'r', label="BF")
ax2.set_ylabel('BF [%]')


fig.autofmt_xdate()
fig.legend(loc="upper right")
plt.title('Body Composition')
# plt.savefig('body_comp.jpg')
plt.show()
