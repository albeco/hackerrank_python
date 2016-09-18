"""
https://www.hackerrank.com/challenges/np-mean-var-and-std
Language: Python 3

Sample Input

2 2
1 2
3 4

Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""

import numpy as np
n, m = (int(x) for x in input().split())
mat1 = np.array([input().split() for _ in range(n)], int)
print(np.mean(mat1, axis=1))
print(np.var(mat1, axis=0))
print(np.std(mat1, axis=None))
