"""
https://www.hackerrank.com/challenges/np-zeros-and-ones
Language: Python 3

Sample Input

3 3 3

Sample Output

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]] 
"""

import numpy as np
sizes = tuple(int(x) for x in input().split())
print(np.zeros(sizes, dtype=np.int))
print(np.ones(sizes, dtype=np.int))
