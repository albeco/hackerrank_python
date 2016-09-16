"""
https://www.hackerrank.com/challenges/designer-door-mat
language: Python 3

Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

n, m = map(int,input().split())
for i in range(n//2): print((".|."*i + ".|." + ".|."*i).center(m,'-')) 
print("WELCOME".center(m,'-'))
for i in range(n//2-1,-1,-1): print((".|."*i + ".|." + ".|."*i).center(m,'-')) 