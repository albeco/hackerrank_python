"""
https://www.hackerrank.com/challenges/write-a-function
language: Python 3

Sample Input

1990  

Sample Output

False  
"""

def is_leap(year):
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        leap = False
    else:
        leap = True
    return leap