"""
https://www.hackerrank.com/challenges/find-a-string
language: Python 3

Sample Input

ABCDCDC
CDC

Sample Output

2
"""

s1 = input()
s2 = input()
n = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        n += 1
print(n)
