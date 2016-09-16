"""
https://www.hackerrank.com/challenges/py-introduction-to-sets
language: Python 3

Sample Input

10
161 182 161 154 176 170 167 171 170 174

Sample Output

169.375
"""

n = input()
mean = lambda values : sum(x for x in values)/len(values)
average_height = mean({int(height) for height in input().split()})
print(average_height)