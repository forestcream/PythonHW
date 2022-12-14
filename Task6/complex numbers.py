import math
from math import sqrt


class Complex:
    def __init__(self, re=0, imag=0):
        self.real = re
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.image)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.real)

    def __truediv__(self, other):
        divisor = (other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real) -
                       (self.imag * other.imag) / divisor,
                       (self.imag * other.real) + (self.real * other.imag) / divisor)

    def __abs__(self):
        new = (self.real ** 2 + (self.imag ** 2) * -1)
        return Complex(sqrt(new.real))

    def __str__(self):
        return "{} {} {}i".format(self.real, '+' if self.imag >= 0 else '-', abs(self.imag))


i = complex(2, 10j)
k = complex(3, 5j)

print(i)
print(k)
