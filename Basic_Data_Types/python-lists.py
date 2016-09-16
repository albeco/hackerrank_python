"""
https://www.hackerrank.com/challenges/python-lists
language: Python 3

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

n = int(input())
ar = []
for _ in range(n):
    command = input().split()
    func = command[0]
    if func=='print':
        print(ar)
    elif func=='pop':
        ar.pop()
    elif func=='reverse':
        ar.reverse()
    elif func=='sort':
        ar.sort()
    elif func=='remove':
        ar.remove(int(command[1]))
    elif func=='append':
        ar.append(int(command[1]))
    elif func=='insert':
        ar.insert(int(command[1]),int(command[2]))