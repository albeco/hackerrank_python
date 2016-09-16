"""
https://www.hackerrank.com/challenges/text-wrap
language: Python 3

Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  
"""

from textwrap import fill
s = input()
w = int(input())
print(fill(s,w))
