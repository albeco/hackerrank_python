"""
https://www.hackerrank.com/challenges/validating-uid
Language: Python 3

Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid
"""

import re
check_10chars = lambda s: bool(re.fullmatch(r'[a-zA-Z0-9]{10}', s))
check_2upper = lambda s: bool(re.search(r'[A-Z]\w*[A-Z]', s))
check_3dgt = lambda s: bool(re.search(r'(\d\w*){3,}', s))
check_reps = lambda s: not bool(re.search(r'(\w)\w*\1', s))
checkUID = lambda s: (check_10chars(s) and check_2upper(s) and check_3dgt(s) and check_reps(s))   

for _ in range(int(input())):
    if checkUID(input().strip()):
        print('Valid')
    else:
        print('Invalid')
