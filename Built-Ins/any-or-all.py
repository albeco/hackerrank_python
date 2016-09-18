"""
https://www.hackerrank.com/challenges/any-or-all
Language: Python 3

Sample Input

5
12 9 61 5 14

Sample Output

True
"""

n, ar = (int(input()), input().split())
print(all(int(x)>0 for x in ar) and any(x==x[::-1] for x in ar))
