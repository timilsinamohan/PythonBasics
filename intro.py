import my_modeule as mm
from my_modeule import find_index, test
import sys
import random
import math
import datetime
import calendar
import os
import webbrowser

# webbrowser.open("https://xkcd.com/353/")

courses = ['History', 'Math','Physics','CompSci']

# index = mm.find_index(courses,'Math')
index = find_index(courses,'Math')
# print(index,test)
print(sys.path)

random_courses = random.choice(courses)
print(random_courses)
rads = math.radians(90)
print(rads)
today = datetime.date.today()
print(today)

print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)
