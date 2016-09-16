"""
https://www.hackerrank.com/challenges/python-quest-1
language: Python 3

Sample Input

5

Sample Output

1
22
333
4444
"""

for i in range(1,int(input())): 
    print((10**i-1)//9*i)
