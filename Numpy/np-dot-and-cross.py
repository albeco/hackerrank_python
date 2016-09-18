"""
https://www.hackerrank.com/challenges/np-dot-and-cross
Language: Python 3

Sample Input

2
1 2
3 4
1 2
3 4

Sample Output

[[ 7 10]
 [15 22]]
"""

import numpy as np
n = int(input())
mat1 = np.array([input().split() for _ in range(n)], int)
mat2 = np.array([input().split() for _ in range(n)], int)
print(np.dot(mat1,mat2))
