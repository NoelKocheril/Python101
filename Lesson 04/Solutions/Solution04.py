# Recursive Solution for converting a string to Integer

import unittest


def asciiToInteger(string: str, num: int = 0) -> int:
    if len(string) == 1:
        return int(string) + (num * 10)

    num = int(string[0]) + (num * 10)
    return asciiToInteger(string[1:], num)


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
