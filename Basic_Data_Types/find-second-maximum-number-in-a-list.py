"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
language: Python 3

Sample Input

5
2 3 6 6 5

Sample Output

5
"""

n = int(input())
ar = list({int(x) for x in input().split()})
ar.sort()
print(ar[-2])