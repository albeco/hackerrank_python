"""
https://www.hackerrank.com/challenges/matrix-script
Language: Python 3

Sample Input

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Sample Output

This is Matrix#  %!
"""

import re

n, m = (int(x) for x in input().split())
s = []
for _ in range(n):
    s.append(input())
t = ''.join(s[i][j] for j in range(m) for i in range(n))
t = re.sub('(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])',' ',t)
print(t)
