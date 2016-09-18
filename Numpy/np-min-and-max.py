"""
https://www.hackerrank.com/challenges/np-min-and-max
Language: Python 3

Sample Input

4 2
2 5
3 7
1 3
4 0

Sample Output

3
"""

from numpy import array, max, min
n, m = (int(x) for x in input().split())
mat1 = array([input().split() for _ in range(n)], int)
print(max(min(mat1, axis=1)))
