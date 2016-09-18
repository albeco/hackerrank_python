"""
https://www.hackerrank.com/challenges/np-concatenate
Language: Python 3

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""

import numpy as np
n, m, p = (int(x) for x in input().split())
ar1 = np.array([input().split() for _ in range(n)], int)
ar2 = np.array([input().split() for _ in range(m)], int)
print(np.concatenate((ar1, ar2)))
