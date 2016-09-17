"""
https://www.hackerrank.com/challenges/word-order
Language: Python 3

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1
"""

from collections import OrderedDict
n = int(input())
rec = OrderedDict()
for _ in range(n):
    entry = input()
    if entry in rec:
        rec[entry] += 1
    else:
        rec[entry] = 1

print(len(rec))
print(*rec.values())
