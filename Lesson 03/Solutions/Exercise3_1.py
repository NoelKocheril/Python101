import unittest

# Given a list of integers, print out the list of the squares of those integers


def squareOfNumbers(myList: list) -> list:

    # Solution #1: Loop through list with for
    # newList = []
    # for i in range(len(myList)):
    #     newList.append(myList[i] * myList[i])

    # return newList

    # Solution #2: Using enumerate
    # newList = []
    # for idx, val in enumerate(len(myList)):
    #     newList.append(val * val)

    # return newList

    # Solution #3: Using in keyword
    # newList = []
    # for  val in myList:
    #     newList.append(val * val)

    # return newList

    # Solution #4: List Comprehesion
    return [x ** 2 for x in myList]


# Tester info, do not change anything below
class squareOfNumbersTester(unittest.TestCase):
    def test_01(self):
        self.assertEqual(
            squareOfNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        )

    def test_02(self):
        self.assertEqual(
            squareOfNumbers([36, 50, 15]),
            [1296, 2500, 225],
        )

    def test_03(self):
        self.assertEqual(
            squareOfNumbers(
                [7, 56, 28, 50, 17, 96, 29, 83, 54, 75, 86, 81, 93, 48, 59]
            ),
            [
                49,
                3136,
                784,
                2500,
                289,
                9216,
                841,
                6889,
                2916,
                5625,
                7396,
                6561,
                8649,
                2304,
                3481,
            ],
        )


if __name__ == "__main__":
    unittest.main()
