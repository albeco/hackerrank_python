"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
language: Python 3

Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""

from itertools import combinations_with_replacement
s, k = input().split()
print(*(''.join(c) for c in combinations_with_replacement(sorted(s),int(k))), sep='\n')