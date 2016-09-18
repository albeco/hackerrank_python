"""
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
Language: Python 3

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""

import re

n = int(input())
s = [input().strip() for _ in range(n)]

d =filter(lambda x: re.search('^[-a-zA-Z0-9_]+@[a-zA-Z0-9]+\.\w{1,3}$', x), s)
print(sorted(d))
