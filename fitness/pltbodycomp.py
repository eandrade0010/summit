#! /usr/bin/env python3

import matplotlib.pyplot as plt

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
    dates.append(line[0])
    weight.append(float(line[1]))
    bf.append(float(line[2]))
    goal.append(line[3])
    print(line)

print(dates)
print(weight)
print(bf)
