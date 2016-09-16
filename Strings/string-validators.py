"""
https://www.hackerrank.com/challenges/string-validators
language: Python 3

Sample Input

qA2

Sample Output

True
True
True
True
True
"""

s =  input()

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))