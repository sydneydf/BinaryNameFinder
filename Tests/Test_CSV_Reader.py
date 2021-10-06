import unittest

from Classes.CSV_Reader import Csv_Reader


class Test_CSV_Reader(unittest.TestCase):
    def setUp(self):
        self.reader = Csv_Reader()

    def tearDown(self):
        pass

    def test_working(self):
        approx_count = 1780
        player_list = self.reader.read_file("/Users/maxim/Desktop/Repos/Python/BinaryNameFinder/chess-players.csv")
        print(player_list[500])
        self.assertGreaterEqual(len(player_list), approx_count)


if __name__ == '__main__':
    unittest.main()
