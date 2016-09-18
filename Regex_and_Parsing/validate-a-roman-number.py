"""
https://www.hackerrank.com/challenges/validate-a-roman-number
Language: Python 3

Sample Input

CDXXI

Sample Output

True
"""

import re
patt = r'M{,3}((CM)|(CD)|(D?C{,3}))((XC)|(XL)|(L?X{,3}))((IX)|(IV)|(V?I{,3}))'
isvalid = lambda x: re.fullmatch(patt, x) != None

print(isvalid(input()))

