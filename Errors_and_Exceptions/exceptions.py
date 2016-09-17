"""
https://www.hackerrank.com/challenges/exceptions
Language: Python 3

Sample Input

3
1 0
2 $
3 1

Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""

for _ in range(int(input())):
    try:
        a, b = (int(x) for x in input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)
