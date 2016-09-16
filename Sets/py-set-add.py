"""
https://www.hackerrank.com/challenges/py-set-add
language: Python 3

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 

Sample Output

5
"""

n = int(input())
countries = set()
for _ in range(n):
    countries.add(input())
print(len(countries))