"""Simple linear algebra library implemented for
fun, and for a somewhat challenging exercise

author: Jack Westcott
"""

class Vector(object):
    def __init__(self, args):
        self.args = [float(x) for x in args]

    def __str__(self):
        return f"{self.args}"


    def __add__(self, alt):
        return Vector(sum(pair) for pair in zip(self.args, alt.args))

    def __sub__(self, alt):
        return Vector(self - alt for self, alt in zip(self.args, alt.args))

    def dot(self, alt):
        return Vector(self * alt for self, alt in zip(self.args, alt.args))
