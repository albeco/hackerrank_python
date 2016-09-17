"""
https://www.hackerrank.com/challenges/incorrect-regex
Language: Python 3

Sample Input

2
.*\+
.*+

Sample Output

True
False
"""

import re
for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
        
