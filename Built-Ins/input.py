"""
https://www.hackerrank.com/challenges/input
Language: Python 2

Sample Input

1 4
x**3 + x**2 + x + 1

Sample Output

True
"""

x, k = (int(x) for x in raw_input().split())
p = input()
print (p==k)
