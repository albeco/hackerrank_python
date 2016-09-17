"""
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
Language: Python 3

Sample Input

2 1
5 6

Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""

import math
class complex:
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return complex(re, im)
    def __sub__(self, other):
        re = self.re - other.re
        im = self.im - other.im
        return complex(re, im)
    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return complex(re, im)
    def conj(self):
        return complex(self.re, -self.im)
    def norm(self):
        return self.re**2 + self.im**2
    def __abs__(self):
        return complex(math.sqrt(self.norm()),0)
    def __truediv__(self, other):
        num = self * other.conj()
        den = other.norm()
        return complex(num.re/den, num.im/den)
    def __str__(self):
        return '{:.2f}{:+.2f}i'.format(self.re, self.im)
    def __repr__(self):
        return 'complex({},{})'.format(self.re, self.im)
        
a = complex(*(float(x) for x in input().split()))
b = complex(*(float(x) for x in input().split()))
print(a+b, a-b, a*b, a/b, abs(a), abs(b), sep='\n')
