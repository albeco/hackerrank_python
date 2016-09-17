"""
https://www.hackerrank.com/challenges/python-time-delta
Language: Python 3

Sample Input

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000

Sample Output

25200
88200
"""

from datetime import datetime

tf = '%a %d %b %Y %H:%M:%S %z'
t = int(input())
for _ in range(t):
    x1 = datetime.strptime(input(), tf)
    x2 = datetime.strptime(input(), tf)
    dt = x1-x2
    print(int(abs(dt.total_seconds())))
