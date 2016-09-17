"""
https://www.hackerrank.com/challenges/calendar-module
Language: Python 3

Sample Input

08 05 2015

Sample Output

WEDNESDAY
"""

from calendar import weekday, day_name
mm, dd, yy = (int(x) for x in input().split())
print(day_name[weekday(yy,mm,dd)].upper())
