"""
https://www.hackerrank.com/challenges/defaultdict-tutorial
Language: Python 3

Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5
"""

import collections as cl

n, m = (int(x) for x in input().split())
A = cl.defaultdict(list)
for i in range(n):
    lett = input()
    A[lett].append(i+1)
    
for _ in range(m):
    lett = input()
    if lett in A:
        print(*A[lett])
    else:
        print(-1)
