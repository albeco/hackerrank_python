"""
https://www.hackerrank.com/challenges/np-array-mathematics
Language: Python 3

Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
"""

import numpy as np

n, m = (int(x) for x in input().split())
mat1 = np.array([input().split() for _ in range(n)], int)
mat2 = np.array([input().split() for _ in range(n)], int)

for op in (np.add, np.subtract, np.multiply, np.floor_divide, np.mod, np.power):
    print(op(mat1, mat2))
