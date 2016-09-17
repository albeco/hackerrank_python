"""
https://www.hackerrank.com/challenges/collections-counter
Language: Python 3

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200
"""

import collections as cl

no_items = int(input())
sizes = cl.Counter(int(x) for x in input().split())
no_cust = int(input())
bids = []
for _ in range(no_cust):
    bids.append(tuple(int(x) for x in input().split()))

cash = 0
for b in bids:
    if sizes[b[0]]>0:
        sizes.subtract([b[0]])
        cash += b[1]
        
print(cash)
