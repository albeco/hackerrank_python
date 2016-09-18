"""
https://www.hackerrank.com/challenges/validating-postalcode
Language: Python 3

Sample Input

110000

Sample Output

False
"""

import re
find_reps = re.compile(r'(\d)(\d)\1\2|(\d)\d\3.*(\d)\d\4')

pcode = input()
validity = re.search('\d+',pcode) and 100000<=int(pcode)<=999999 and not find_reps.search(pcode)
print(bool(validity))
