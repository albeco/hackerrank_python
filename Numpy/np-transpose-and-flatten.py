"""
https://www.hackerrank.com/challenges/np-transpose-and-flatten
Language: Python 3

Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]
"""

import numpy as np

n, m = (int(x) for x in input().split())
ar = np.array([[int(x) for x in input().split()] for _ in range(n)])
print(np.transpose(ar))
print(ar.flatten())
