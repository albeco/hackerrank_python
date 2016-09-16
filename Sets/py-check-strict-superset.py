"""
https://www.hackerrank.com/challenges/py-check-strict-superset
language: Python 3

Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output

False
"""

A = {int(x) for x in input().split()}
N = int(input())
result = True
for _  in range(N):
    B = {int(x) for x in input().split()}
    if not A>B:
        result = False
        break
        
print(result)