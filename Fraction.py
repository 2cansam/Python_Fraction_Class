"""Samuel Hubbard
   10/15/2021
   Fraction Python Class"""
import math
import sympy as sym


class Fraction:

    def __init__(self, numerator, denominator):
        """Takes in 2 numbers and finds the GCD of both then simplifies them."""
        gcd = math.gcd(numerator, denominator)
        self.top = sym.simplify(numerator) // gcd
        self.bottom = sym.simplify(denominator) // gcd

    def __str__(self):
        """Converts output to a string"""
        if self.bottom == 1:
            return str(self.top)
        elif self.top > self.bottom:
            return str(self.top // self.bottom) + " " + str(Fraction(self.top % self.bottom, self.bottom))
        else:
            return str(self.top) + "/" + str(self.bottom)

    def double(self):
        """Multiplies fraction by the number 2"""
        return Fraction(2 * self.top, self.bottom)

    def multiply(self, n):
        """Multiplies fraction by a given number"""
        return Fraction(n * self.top, self.bottom)

    def __add__(self, other):
        """Adds two given fractions"""
        newtop = self.top * other.bottom + other.top * self.bottom
        newbottom = self.bottom * other.bottom
        return Fraction(newtop, newbottom)

    def __sub__(self, other):
        """Subtracts two given fractions"""
        newtop = (self.top * other.bottom) - (self.bottom * other.top)
        newbottom = math.lcm(self.bottom, other.bottom)
        return Fraction(newtop, newbottom)

    def __mul__(self, other):
        """Multiplies 2 fractions together"""
        newtop = self.top * other.top
        newbottom = self.bottom * other.bottom
        return Fraction(newtop, newbottom)

    def __truediv__(self, other):
        """Divides 2 fractions"""
        newtop = self.top * other.bottom
        newbottom = self.bottom * other.top
        return Fraction(newtop, newbottom)

    def __lt__(self, other):
        """Less than comparison of 2 fractions"""
        return self.top * other.bottom < other.top * self.bottom

    def __gt__(self, other):
        """Greater than comparison of 2 fractions"""
        return self.top * other.bottom > other.top * self.bottom

    def __eq__(self, other):
        """Checks if 2 fractions are equal to each other"""
        return self.top * other.bottom == other.top * self.bottom

    def __le__(self, other):
        """Checks if 2 fractions are less than or equal to each other"""
        return self < other or self == other

    def __ge__(self, other):
        """Checks if 2 fractions are greater than or equal to each other"""
        return self > other or self == other


f = Fraction(15, 20)
print(f)
print(f.double())
print(f.multiply(5))
print(f + Fraction(1, 10))
print(f - Fraction(2, 5))
print(f * Fraction(3, 12))
print(f / Fraction(4, 15))
print(Fraction(1, 2) > Fraction(3, 4))
print(Fraction(4, 8) < Fraction(6, 10))
print(Fraction(15, 21) == Fraction(5, 7))
print(Fraction(5, 4) <= Fraction(1, 2))
print(Fraction(75, 15) >= Fraction(100, 52))
