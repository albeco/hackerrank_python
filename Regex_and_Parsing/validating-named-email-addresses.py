"""
https://www.hackerrank.com/challenges/validating-named-email-addresses
Language: Python 3

Sample Input

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output

DEXTER <dexter@hotmail.com>
"""

import email.utils
import re

is_valid_email = lambda s: bool(re.fullmatch(r'[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}', s))

n = int(input())
for _ in range(n):
    s = input()
    name, addr = email.utils.parseaddr(s)
    if is_valid_email(addr):
        print(s)
