"""
https://www.hackerrank.com/challenges/python-mod-divmod
language: Python 3

Sample Input

177
10

Sample Output

17
7
(17, 7)
"""

a = input()
b = input()
a, b = int(a), int(b)

print(a//b)
print(a%b)
print(divmod(a,b))