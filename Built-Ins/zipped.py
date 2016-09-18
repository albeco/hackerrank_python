"""
https://www.hackerrank.com/challenges/zipped
Language: Python 3

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output

90.0 
91.0 
82.0 
90.0 
85.5
"""

n, x = (int(x) for x in input().split())
studs = []
for _ in range(x):
    studs.append([float(x) for x in input().split()])
    
for subj in zip(*studs):
    print(sum(subj)/x)
