"""
https://www.hackerrank.com/challenges/polar-coordinates
language: Python 3

Sample Input

  1+2j
  
Sample Output

 2.23606797749979 
 1.1071487177940904
"""

from cmath import phase
z = complex(input())
print(abs(z))
print(phase(z))