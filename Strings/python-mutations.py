"""
https://www.hackerrank.com/challenges/python-mutations
language: Python 3

Sample Input

abracadabra
5 k

Sample Output

abrackdabra
"""

s = input()
subs = input().split()
i, c = int(subs[0]), subs[1]
print(s[:i]+c+s[i+1:])

