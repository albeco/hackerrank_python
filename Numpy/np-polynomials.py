"""
https://www.hackerrank.com/challenges/np-polynomials
Language: Python 3

Sample Input

1.1 2 3
0

Sample Output

3.0
"""

import numpy as np
ar = np.array(input().split(), float)
x = float(input())
print(np.polyval(ar, x))
