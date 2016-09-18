"""
https://www.hackerrank.com/challenges/np-linear-algebra
Language: Python 3

Sample Input

2
1.1 1.1
1.1 1.1

Sample Output

0.0
"""

import numpy as np
n = int(input())
mat = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(mat))
