import datetime
import time
import re
from sortedcontainers import SortedList

with open("input.txt") as file:
    lines = file.readlines()

########## Regex grammars ##########
# Split timestamp and memo
splitTime = re.compile(r'\[(.+)\]\s(.+)')
# Get guard number from memo
guardNum = re.compile(r'Guard \#([0-9]+)')

########## Time Processing ##########
# Timestamps are written using year-month-day hour:minute format.
timeFormat = '%Y-%m-%d %H:%M'

def parse(lst):
    """Return two-tuple of datetime object and memo"""
    parsedData = SortedList()
    for string in lst:
        parts = splitTime.search(string)
        timeString = parts[1]
        memo = parts[2]
        dt = datetime.datetime.strptime(timeString, timeFormat)
        parsedData.add((dt,memo))
    return parsedData
