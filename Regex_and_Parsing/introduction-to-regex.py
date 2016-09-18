"""
https://www.hackerrank.com/challenges/introduction-to-regex
Language: Python 3

Sample Input

4  
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output

False
True
True
False
"""

import re

n = int(input())
for _ in range(n):
    print(bool(re.match(r'^[+-]?\d*\.\d+$', input())))
