"""
https://www.hackerrank.com/challenges/most-commons
Language: Python 3

Sample Input

aabbbccde

Sample Output

b 3
a 2
c 2
"""

import collections as cl
c = cl.Counter(input())
s = sorted(c.items(), key = lambda x: x[0])
s = sorted(s,reverse=True, key = lambda x: x[1])
for i in range(3):
    print(*s[i])
