import unittest
import time

from Classes.BinarySearch import BinarySearch


class Test_BinarySearch(unittest.TestCase):
    def setUp(self):
        self.BinarySearch = BinarySearch()

    def test_BSearchFind(self):
        # Activates recursive function
        playerFound = self.BinarySearch.bSearch("Firmian")
        print(playerFound)
        self.assertEqual("Firmian", playerFound.lastName)


if __name__ == '__main__':
    unittest.main()
