import math
import unittest
from complex_numbers import Complex


class MyTestCase(unittest.TestCase):
    def test_add(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(3, 1)
        expected = Complex(5, 4)

        actual = number_1 + number_2

        self.assertEqual(str(expected), str(actual))

    def test_sub(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(3, 1)
        expected = Complex(-1, 2)

        actual = number_1 - number_2

        self.assertEqual(str(expected), str(actual))

    def test_mul(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(3, 1)
        expected = Complex(3, 11)

        actual = number_1 * number_2

        self.assertEqual(str(expected), str(actual))

    def test_truediv(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(3, 1)
        expected = Complex(0.9, 0.7)

        actual = number_1 / number_2

        self.assertEqual(str(expected), str(actual))

    def test_abs(self):
        number = Complex(1, 3)
        expected = math.sqrt(10)

        actual = abs(number)

        self.assertEqual(str(expected), str(actual))

    def test_str(self):
        number = Complex(1, 3)
        expected = "1+3i"
        actual = str(number)

        self.assertEqual(str(expected), str(actual))


if __name__ == '__main__':
    unittest.main()
