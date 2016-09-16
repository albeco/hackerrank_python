"""
https://www.hackerrank.com/challenges/finding-the-percentage
language: Python 3

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00
"""

n = int(input())
marks = {}
for _ in range(n):
    name, mark0, mark1, mark2 = input().split()
    marks[name] = tuple(float(x) for x in (mark0,mark1,mark2))
s = input()
print('{:.2f}'.format(sum(marks[s])/3))