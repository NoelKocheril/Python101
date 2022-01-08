import unittest

# Given a list of numbers, I want you to return the sum of only the positive numbers


def sumOfPositiveNumbers(listOfItems: list) -> int:

    # Solution #1: Basic Loop
    # mySum = 0
    # for i in range(len(listOfItems)):
    #     if listOfItems[i] > 0:
    #         mySum += listOfItems[i]
    # return mySum

    # Solution  #2: Using enumerate
    # mySum = 0
    # for idx, val in enumerate(listOfItems):
    #     if val > 0:
    #         mySum += val
    # return mySum

    # Solution  #3: Using in
    # mySum = 0
    # for val in listOfItems:
    #     if val > 0:
    #         mySum += val
    # return mySum

    # Solution #4: List Comprehesion
    return sum([x for x in listOfItems if x > 0])


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
