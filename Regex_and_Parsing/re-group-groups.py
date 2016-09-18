"""
https://www.hackerrank.com/challenges/re-group-groups
Language: Python 3

Sample Input

..12345678910111213141516171820212223

Sample Output

1
"""

import re
x = re.search(r'([a-zA-Z0-9])(?=\1)',input())
print(x.group(1) if x else -1)

