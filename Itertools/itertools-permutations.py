"""
https://www.hackerrank.com/challenges/itertools-permutations
language: Python 3

Sample Input

HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

from itertools import permutations
s, k = input().split()
k = int(k)
for p in sorted(permutations(s,k)):
    print(''.join(p))