"""
https://www.hackerrank.com/challenges/map-and-lambda-expression
Language: Python 3

Sample Input

5

Sample Output

[0, 1, 1, 8, 27]
"""

fib = lambda n: (0,1,1)[n] if n<3 else fib(n-1)+fib(n-2)
fib_no = map(fib, range(int(input())))
print(list(map(lambda x:x**3, fib_no)))
