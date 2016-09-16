"""
https://www.hackerrank.com/challenges/symmetric-difference
language: Python 3

Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output

5
9
11
12
"""

n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

for x in sorted(s1.union(s2) - s1.intersection(s2)):
    print(x)