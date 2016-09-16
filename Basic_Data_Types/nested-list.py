"""
https://www.hackerrank.com/challenges/nested-list
language: Python 3

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry
"""

n = int(input())
scores = []
for _ in range(n):
    name = input()
    grade = float(input())
    scores.append([name, grade])
    
givengrades = sorted({x[1] for x in scores})
sts = sorted(x[0] for x in scores if x[1]==givengrades[1])
for s in sts:
    print(s)