"""
https://www.hackerrank.com/challenges/maximize-it
language: Python 3

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206
"""

import itertools as itt

k, m = map(int, input().split())
ar = []
for _ in range(k):
    x = [int(i) for i in input().split()]
    ar.append(x[1:])

f = lambda x: sum(k*k for k in x) % m

print(max(map(f, itt.product(*ar))))
