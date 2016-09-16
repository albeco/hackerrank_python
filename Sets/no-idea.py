"""
https://www.hackerrank.com/challenges/no-idea
language: Python 3

Sample Input

3 2
1 5 3
3 1
5 7

Sample Output

1
"""

n, m = (int(x) for x in input().split())
ar = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
print(len([x for x in ar if x in A])-len([x for x in ar if x in B]))
