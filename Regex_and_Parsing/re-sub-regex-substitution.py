"""
https://www.hackerrank.com/challenges/re-sub-regex-substitution
Language: Python 3

Sample Input

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

import re
text = []
n = int(input())
for i in range(n):
    s = input()
    s = re.sub('(?<=\s)&&(?=\s)','and', s)
    s = re.sub('(?<=\s)\|\|(?=\s)','or', s)
    text.append(s)
for s in text:
    print(s)
