"""
https://www.hackerrank.com/challenges/np-inner-and-outer
Language: Python 3

Sample Input

0 1
2 3

Sample Output

3
[[0 0]
 [2 3]]
"""

import numpy as np
ar1 = np.array(input().split(), int)
ar2 = np.array(input().split(), int)
print(np.inner(ar1, ar2))
print(np.outer(ar1, ar2))
