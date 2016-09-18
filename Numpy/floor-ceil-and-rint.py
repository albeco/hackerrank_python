"""
https://www.hackerrank.com/challenges/floor-ceil-and-rint
Language: Python 3

Sample Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""

import numpy as np
ar = np.array(input().split(), float)
print(np.floor(ar))
print(np.ceil(ar))
print(np.rint(ar))
