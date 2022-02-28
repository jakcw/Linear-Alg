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

    @property
    def length(self):
        return len(self.args)

    @property
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

class Matrix(object):
    def __init__(self, *args):

        """If we instantiate a matrix object with two arguments, we want these two arguments
        (which will be integers) to be the number of rows and columns. This will construct
        a matrix of zeroes with args[0] rows and args[1] columns"""

        if len(args) == 2:
            self.rows = args[0]
            self.cols = args[1]
            self.args = [[float(0) for x in range(self.cols)] for x in range(self.rows)]
        elif len(args) == 1:
            try:
                self.rows = len(args[0])
                self.cols = len(args[0][0])
                self.args = [[float(x) for x in row] for row in args[0]]
            except:
                raise MatError("Cannot construct. For row or column vectors, instantiate vector object.")

    def __str__(self):
        return f"{self.args}"


    """Properties used for computations within other methods"""
    @property
    def dim(self):
        return (self.rows, self.cols)

    @property
    def m(self):
        return self.rows

    @property
    def n(self):
        return self.cols


    def __add__(self, alt):
        return Matrix([[sum(pair) for pair in zip(self.args[x], alt.args[x])] for x in range(self.rows)])

    def __sub__(self, alt):
        return Matrix([[self.args[x] - alt.args[x] for self.args[x], alt.args[x] in zip(self.args[x], alt.args[x])] for x in range(self.rows)])


    def square(self):
        """test if matrix is square (nxn)"""
        return self.m == self.n

    def det(self):
        result = 0
        if self.square() and self.m == 2:
            return (self.args[0][0]  * self.args[1][1]) - (self.args[0][1] * self.args[1][0])
