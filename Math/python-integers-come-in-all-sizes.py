"""
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes
language: Python 2

Sample Input

9
29
7
27

Sample Output

4710194409608608369201743232  
"""

def readint():
    return int(raw_input())
a,b,c,d = (readint() for _ in range(4))
print a**b + c**d