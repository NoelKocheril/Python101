import unittest

# Given a list of items, I want you to return whether or not there are duplicate items


def areThereDuplicates(listOfItems: list) -> bool:
    setOfItems = set(listOfItems)
    return len(setOfItems) != len(listOfItems)


# Tester info, do not change anything below
class areThereDuplicatesTester(unittest.TestCase):
    def test_01(self):
        self.assertEqual(areThereDuplicates([1, 2, 3, 4, 5, 5, 6, 8, 9, 10]), True)

    def test_02(self):
        self.assertEqual(areThereDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), False)

    def test_03(self):
        self.assertEqual(areThereDuplicates([1, 1, 1, 1, 1, 1, 1]), True)


if __name__ == "__main__":
    unittest.main()
