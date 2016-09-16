"""
https://www.hackerrank.com/challenges/list-comprehensions
language: Python 3

Sample Input

1
1
1
2

Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

grid = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if not i+j+k==n]

print(grid)