#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filter", help="You can choose to reduce noise of data", action='store_true')
parser.add_argument("--type", help="Define either 'bulk' or 'cut'")
parser.add_argument("--save", help="Will save as jpg", action="store_true")
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


# ==========================================================
# AVERAGES
# ==========================================================
avg_weight = [0]*len(weight)
avg_bf = [0]*len(bf)
for i in range(len(weight)):
    if i == 0:
        avg_weight[i]= (weight[i]+weight[i+1])/2
        avg_bf[i]= (bf[i]+bf[i+1])/2
    elif i == len(weight)-1:
        avg_weight[i] = (weight[i]+weight[i-1])/2
        avg_bf[i] = (bf[i]+bf[i-1])/2
    else:
        avg_weight[i] = (weight[i-1]+weight[i]+weight[i+1])/3
        avg_bf[i] = (bf[i-1]+bf[i]+bf[i+1])/3


# ==========================================================
# CHANGES
# ==========================================================
change_weight = []
week = []
for i in range(0,len(weight)-7,7):
    week.append(int(i/7))
    change_weight.append(weight[i+7]-weight[i])

weight = avg_weight
bf = avg_bf


#
# print(change_weight)

# PLOTTING
fig1, ax1 = plt.subplots()
ax1.plot_date(dates, weight, 'k', label="Weight")
ax1.set_xlabel('Date')
ax1.set_ylabel('Weight [lbs]')

ax2 = ax1.twinx()
ax2.plot_date(dates, bf, 'r', label="BF")
ax2.set_ylabel('BF [%]')

# ax3.plot(week,change_weight, '--k', label="Change in Weight")

# ax4 = ax3.twinx()
# ax4.plot_date(dates, change_bf, '--r', label="Change in BF")

fig1.autofmt_xdate()
fig1.legend(loc="upper right")

fig1.suptitle('Body Composition with Average Filter')

fig2, ax3 = plt.subplots()
ax3.plot(week, change_weight, 'k', label="Change in Weight")
# ax4 = ax3.twinx()
# ax4.plot(week, change_bf, 'r', label="Change in BF")
# ax4.

if args.save: fig1.savefig('body_comp.jpg')
plt.show()
# print(avg_weight)
