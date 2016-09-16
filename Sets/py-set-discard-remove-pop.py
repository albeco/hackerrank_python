"""
https://www.hackerrank.com/challenges/py-set-discard-remove-pop
language: Python 3

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4
"""

no_el = int(input())
x = {int(x) for x in input().split()}
no_comm = int(input())
for _ in range(no_comm):
    comm = input().split()
    if comm[0]=='remove':
        x.remove(int(comm[1]))
    elif comm[0]=='discard':
        x.discard(int(comm[1]))
    elif comm[0]=='pop':
        temp = x.pop()
print(sum(x))

