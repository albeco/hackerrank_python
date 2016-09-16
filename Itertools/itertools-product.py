"""
https://www.hackerrank.com/challenges/itertools-product
language: Python 3

Sample Input

 1 2
 3 4
 
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
"""

from itertools import product
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*(product(a,b)))