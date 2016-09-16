"""
https://www.hackerrank.com/challenges/py-set-intersection-operation
language: Python 3

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

5
"""

_ = int(input())
n = {int(x) for x in input().split()}
_ = int(input())
b = {int(x) for x in input().split()}
print(len(n.intersection(b)))