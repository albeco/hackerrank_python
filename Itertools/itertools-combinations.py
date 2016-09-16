"""
https://www.hackerrank.com/challenges/itertools-combinations
language: Python 3

Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""

from itertools import combinations

s, k = input().split()
s, k = sorted(s), int(k)

combs = [''.join(c) for i in range(1,k+1) for c in combinations(s,i)]

print(*combs,sep='\n')