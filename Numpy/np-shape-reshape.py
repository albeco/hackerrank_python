"""
https://www.hackerrank.com/challenges/np-shape-reshape
Language: Python 3

Sample Input

1 2 3 4 5 6 7 8 9

Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

import numpy as np
x = np.array(input().split(), int)
print(x.reshape(3,3))
