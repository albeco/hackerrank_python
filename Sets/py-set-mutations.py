"""
https://www.hackerrank.com/challenges/py-set-mutations
language: Python 3

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
 
Sample Output

38
"""

_ = int(input())
A = {int(x) for x in input().split()}
N = int(input())
for _ in range(N):
    op, _ = input().split()
    B = {int(x) for x in input().split()}
    if op=='update':
        A.update(B)
    elif op=='intersection_update':
        A.intersection_update(B)
    elif op=='difference_update':
        A.difference_update(B)
    elif op=='symmetric_difference_update':
        A.symmetric_difference_update(B)
print(sum(A))