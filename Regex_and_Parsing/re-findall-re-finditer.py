"""
https://www.hackerrank.com/challenges/re-findall-re-finditer
Language: Python 3

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output

ee
Ioo
Oeo
eeeee
"""

import re
s = input()
x = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)
if x:
    print(*x, sep='\n')
else:
    print(-1)
