"""
https://www.hackerrank.com/challenges/find-angle
language: Python 3

Sample Input

10
10

Sample Output

45°
"""

from math import acos, pi, sqrt

ab = int(input())
bc = int(input())

ac = sqrt(ab**2 + bc**2)
bm = sqrt(ab**2+bc**2)/2

theta = acos((bm**2 + bc**2 - (ac/2)**2)/2/bc/bm)

print(str(int(round(theta/pi*180))) + "°")