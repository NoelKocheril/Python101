import unittest

# Given a list of numbers, I want you to return the sum of only the positive numbers


def sumOfPositiveNumbers(listOfItems: list) -> int:

    # Solution goes here

    return -1


# Tester info, do not change anything below
class sumOfPositiveNumbersTester(unittest.TestCase):
    def test_01(self):
        self.assertEqual(sumOfPositiveNumbers([1, -2, 3, -4, -5, 6, -7, 8, 9, 10]), 37)

    def test_02(self):
        self.assertEqual(sumOfPositiveNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    def test_03(self):
        self.assertEqual(sumOfPositiveNumbers([1, 1, 1, 1, 1, 1, 1]), 7)

    def test_04(self):
        self.assertEqual(sumOfPositiveNumbers([-1, -1, -1, -1, -1, -1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
