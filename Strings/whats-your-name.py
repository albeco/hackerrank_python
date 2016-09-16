"""
https://www.hackerrank.com/challenges/whats-your-name
language: Python 3

Sample Input

Guido
Rossum

Sample Output

Hello Guido Rossum! You just delved into python.
"""

first_name = input()
last_name = input()
print("Hello {} {}! You just delved into python.".format(first_name, last_name))