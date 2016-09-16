"""
https://www.hackerrank.com/challenges/compress-the-string
language: Python 3

Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
"""

from itertools import groupby

res = []
for k, g in groupby(input()):
    res.append((len(list(g)),int(k)))
    
print(*res)