"""
https://www.hackerrank.com/challenges/re-split
Language: Python 3



Sample Input

100,000,000.000

Sample Output

100
000
000
000
"""

import re
print(*filter(None, re.split('[\.,]', input())), sep = '\n')
