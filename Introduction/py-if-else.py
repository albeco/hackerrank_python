'''
https://www.hackerrank.com/challenges/py-if-else
language: Python 3

Sample Input 0

3

Sample Output 0

Weird

Sample Input 1

24

Sample Output 1

Not Weird
'''
n = int(input().strip())
if (n % 2 == 1):
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n>20:
    print("Not Weird")