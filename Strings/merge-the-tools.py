"""
https://www.hackerrank.com/challenges/merge-the-tools
language: Python 3

Sample Input

AABCAAADA
3   

Sample Output

AB
CA
AD
"""

from itertools import zip_longest

def nub(s):
    '''remove duplicates'''
    seen = set()
    for c in s:
        if c not in seen:
            seen.add(c)
            yield c
            
group = lambda s, n: zip_longest(*([iter(s)]*n))
group_uniques = lambda s,n: [''.join(nub(x)) for x in group(s, n)]            


for x in group_uniques(input(), int(input())):
    print(x)