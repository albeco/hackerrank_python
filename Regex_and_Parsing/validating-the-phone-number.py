"""
https://www.hackerrank.com/challenges/validating-the-phone-number
Language: Python 3

Sample Input

2
9587456281
1252478965

Sample Output

YES
NO
"""

import re
n = int(input())
for _ in range(n):
    if re.fullmatch('[789]\d{9}', input()) != None:
        print('YES')
    else:
        print('NO')

