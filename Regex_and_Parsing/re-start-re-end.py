"""
https://www.hackerrank.com/challenges/re-start-re-end
Language: Python 3

Sample Input

aaadaa
aa

Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""

import re
s = input()
k = input()
locs = []
for i in range(len(s)):
    x = re.match(k, s[i:])
    if x:
        locs.append((x.start() + i, x.end() + i - 1))
if locs:
    print(*locs, sep='\n')
else:
    print((-1, -1))
