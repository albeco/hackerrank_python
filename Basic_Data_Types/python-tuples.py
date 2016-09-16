"""
https://www.hackerrank.com/challenges/python-tuples
language: Python 3

Sample Input

2
1 2

Sample Output

3713081631934410656
"""

n = int(input())
t = tuple(int(x) for x in input().split())
print(hash(t))