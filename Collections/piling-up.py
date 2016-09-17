"""
https://www.hackerrank.com/challenges/piling-up
Language: Python 3

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No
"""

from collections import deque
t = int(input())
for _ in range(t):
    _ = input()
    cube_sizes = deque(int(x) for x in input().split())
    base = max(cube_sizes[0], cube_sizes[-1])
    while len(cube_sizes)>0:
        if cube_sizes[-1]>=cube_sizes[0]:
            this = cube_sizes.pop()
        else:
            this = cube_sizes.popleft()
        if this > base:
            print('No')
            break
        else:
            base = this
    else:
        print('Yes')
