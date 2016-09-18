"""
https://www.hackerrank.com/challenges/python-sort-sort
Language: Python 3

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

n, m = (int(i) for i in input().split())
ar = []
for _ in range(n):
    ar.append([int(i) for i in input().split()])
k = int(input())

ar.sort(key = lambda x: x[k])
for x in ar:
    print(*x)
