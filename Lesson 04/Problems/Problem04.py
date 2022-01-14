# Recursive Solution for converting a string to Integer
# No Type Casting or built-in functions, turn the string into it's Integer representation

import unittest


def asciiToInteger(number: str) -> int:
    return -1


class asciiToIntegerTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(asciiToInteger("123"), 123)

    def test_02(self):
        self.assertEqual(asciiToInteger("10056"), 10056)

    def test_03(self):
        self.assertEqual(asciiToInteger("80128"), 80128)

    def test_04(self):
        self.assertEqual(asciiToInteger("80085"), 80085)

    def test_05(self):
        self.assertEqual(asciiToInteger("1337"), 1337)


if __name__ == "__main__":
    unittest.main()
