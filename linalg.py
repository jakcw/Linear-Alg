"""Simple linear algebra library implemented for
fun, and for a somewhat challenging exercise

author: Jack Westcott
"""

import math

class VecError(Exception):
    """Raise VecError on such things like adding vector to scalar,
    or trying to compute cross product of  > 3-dimensional vectors"""
    pass

class Vector(object):

    def __init__(self, args):
        self.args = [float(x) for x in args]

    def __str__(self):
        return f"{self.args}"

    def __add__(self, alt):
        return Vector(sum(pair) for pair in zip(self.args, alt.args))

    def __sub__(self, alt):
        return Vector(self - alt for self, alt in zip(self.args, alt.args))

    def __mul__(self, val):
        """Scalar multiplication"""
        return Vector(self * val for self in self.args)

    def length(self):
        return len(self.args)

    def mag(self):
        result = 0
        for i in range(len(self.args)):
            result += self.args[i] ** 2
        return round(math.sqrt(result), 3)

    def dot(self, alt):
        return Vector(self * alt for self, alt in zip(self.args, alt.args))

    def cross(self, alt):
        if len(self.args) != 3:
            raise VecError("Cross product only defined on vectors of size 3")
        return Vector([self.args[1]*alt.args[2] - self.args[2]*alt.args[1], self.args[2]*alt.args[0] - self.args[0]*alt.args[2],self.args[0]*alt.args[1] - self.args[1]*alt.args[0]])

class MatError(Exception):
    """Raise MatError on such things as matrix multiplication, dimensions of matrix
    A and B must have correct number of rows and cols"""
    pass

class Matrix:
    pass
