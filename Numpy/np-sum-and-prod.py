"""
https://www.hackerrank.com/challenges/np-sum-and-prod
Language: Python 3

Sample Input

2 2
1 2
3 4

Sample Output

24
"""

import numpy as np
n, m = (int(x) for x in input().split())
mat1 = np.array([input().split() for _ in range(n)], int)

print(np.prod(np.sum(mat1, axis=0)))
