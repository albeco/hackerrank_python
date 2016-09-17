"""
https://www.hackerrank.com/challenges/py-collections-ordereddict
Language: Python 3

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

from collections import OrderedDict
n = int(input())
rec = OrderedDict()
for _ in range(n):
    entry = input().split()
    item = ' '.join(entry[:-1])
    price = int(entry[-1])
    if item in rec:
        rec[item] += price
    else:
        rec[item] = price
for item,price in rec.items():
    print(item,price)
    
