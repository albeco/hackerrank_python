"""
https://www.hackerrank.com/challenges/np-eye-and-identity
Language: Python 3

Sample Input

3 3

Sample Output

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""

import numpy as np
n, m = (int(x) for x in input().split())
print(np.eye(n,m))
