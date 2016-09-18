"""
https://www.hackerrank.com/challenges/ginorts
Language: Python 3

Sample Input

Sorting1234

Sample Output

ginortS1324
"""

print(*sorted(input(), key = lambda c: ord(c)+100*c.isupper() if c.isalpha() else ord(c)+1000-100*c.isdigit()*(ord(c)%2)),sep='')
