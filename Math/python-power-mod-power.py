"""
https://www.hackerrank.com/challenges/python-power-mod-power
language: Python 2

Sample Input

3
4
5

Sample Output

81
1
"""

a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

print pow(a,b)
print pow(a,b,m)