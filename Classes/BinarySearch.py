import time

from Classes.CSV_Reader import Csv_Reader


class BinarySearch:

    # Does self.player_list get wiped on init
    def __init__(self):
        self.player_list = None
        self.onAppearing()

    # Designed to have properties filled when class loaded, Similiar to Xamarin onAppearing method

    # activate an instance of our Csv_reader
    # read the file and convert to List of Player objects
    # sort the list based on lastname property of objects
    def onAppearing(self):
        reader = Csv_Reader()
        sorted_players = sorted(reader.read_file(
            "/Users/maxim/Desktop/Repos/Python/BinaryNameFinder/chess-players.csv"), key=lambda player: player.lastName)

        self.player_list = sorted_players

    def bSearch(self, _lastName2Search):
        print("Initiating Search")
        time.sleep(2)

        start_i = 0
        end_i = len(self.player_list)

        loop_count = 0

        while end_i > start_i:
            print(f"Current iteration count: {loop_count}")
            time.sleep(1)
            loop_count += 1
            # Sliced here of reducing list
            print(f"Total Approx Elements left: {len(self.player_list[start_i: end_i])}")
            middle_i = (start_i + end_i) // 2

            # if Middle == SearchedPlayer
            if _lastName2Search == self.player_list[middle_i].lastName:
                # Player found and use __str__ to print object
                print("LastName Found!")
                time.sleep(1)
                return self.player_list[middle_i]

            # if searched name less than current middle than change the end of the list so that we go left of current
            # middle
            elif _lastName2Search < self.player_list[middle_i].lastName:
                end_i = middle_i
            # Search right tree by changing to a new range of middle_i and previous end
            else:
                start_i = middle_i

            # TODO: Add Error for Lastname not spelt correctly
