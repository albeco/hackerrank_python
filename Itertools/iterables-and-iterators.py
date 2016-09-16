"""
https://www.hackerrank.com/challenges/iterables-and-iterators
language: Python 3

Sample Input

4 
a a c d
2

Sample Output

0.8333
"""

import itertools as itt

n = int(input())
s = input().split()
k = int(input())

na = s.count('a')

all_choices = list(itt.combinations(s, k))
good_ones = [choice for choice in all_choices if 'a' in choice]

print(len(good_ones)/len(all_choices))