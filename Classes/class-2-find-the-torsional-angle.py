"""
https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle
Language: Python 3

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2

Sample Output

8.19
"""

import math

class Vector:
    def __init__(self, coord):
        self.coord = coord
    def __str__(self):
        return '{}'.format(self.coord)
    def __repr__(self):
        return 'Vector([{0},{1},{2}])'.format(*self.coord)
    def __add__(self, other):
        return Vector([a+b for (a,b) in zip(self.coord, other.coord)])
    def __sub__(self, other):
        return Vector([a-b for (a,b) in zip(self.coord, other.coord)])
    def dot(self, other):
        return sum(a*b for (a,b) in zip(self.coord, other.coord))
    def norm(self):
        return math.sqrt(self.dot(self))
    def cross(self, other):
        x1, y1, z1 = self.coord
        x2, y2, z2 = other.coord
        x3 = y1 * z2 - z1 * y2
        y3 = z1 * x2 - x1 * z2
        z3 = x1 * y2 - y1 * x2
        return Vector([x3,y3,z3])
    @staticmethod
    def angle_between(v1, v2):
        return math.acos(v1.dot(v2)/v1.norm()/v2.norm())
    
class Plane:
    def __init__(self,A,B,C):
        AB = Vector(B) - Vector(A)
        AC = Vector(C) - Vector(A)
        self.normal = AB.cross(AC)
        self.normal.coord = [t/self.normal.norm() for t in self.normal.coord]

def get_coords():
    return [float(x) for x in input().split()]

A, B, C, D = (get_coords() for _ in range(4))

p1 = Plane(A, B, C)
p2 = Plane(B, C, D)
theta = Vector.angle_between(p1.normal, p2.normal)
print('{:.2f}'.format(theta/math.pi*180))
