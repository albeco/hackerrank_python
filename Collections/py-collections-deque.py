"""
https://www.hackerrank.com/challenges/py-collections-deque
Language: Python 3

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2
"""

from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    com = input().split()
    if com[0]=='append':
        d.append(int(com[1]))
    elif com[0]=='appendleft':
        d.appendleft(int(com[1]))
    elif com[0]=='pop':
        d.pop()
    elif com[0]=='popleft':
        d.popleft()
print(*d)
