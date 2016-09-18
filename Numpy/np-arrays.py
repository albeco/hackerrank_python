"""
https://www.hackerrank.com/challenges/np-arrays
Language: Python 3

Sample Input

1 2 3 4 -8 -10

Sample Output

[-10.  -8.   4.   3.   2.   1.]
"""

import numpy as np
x = np.array([float(x) for x in input().split()])
print(x[-1::-1])
