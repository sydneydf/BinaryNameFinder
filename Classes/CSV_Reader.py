import csv

from Classes.Player import Player


class Csv_Reader:
    def read_file(self, _fileName):
        # Open CSV List

        player_list = []
        # Open passed in filename in reading mode and utf8 encoding for those non-english characters so we can compare them
        with open(_fileName, "r", encoding="utf8") as csv_file:
            # Init a csv Module reader object passing the csv_file into the object
            reader = csv.reader(csv_file)
            # Skip 1 line (Header)
            next(reader, None)
            # Row Unpacking begins
            for _lastName, _firstName, _fullName, _countries, _born, _died in reader:
                # We need to parse _countries into a list, countries is a Quotes string each country seperated by comma

                country_list = []
                # Not Gate Logic here (Inverse), Detect multiple countires
                if "," not in _countries:
                    country_list.append(_countries)
                # Triggers when multiple countries detected
                else:
                    multi_Countries = _countries.split(',')
                    for country in multi_Countries:
                        country_list.append(country)

                # Process the various conditions of the file

                # Custom parameter - Cross reference Player.born() and Player.living() function for what they mean
                if _born == "?":
                    _born = -1
                elif "<" in _born:
                    _born = _born.replace("<", "")
                    _born = int(_born)  # Can we do both statements on same line or will that break?

                if _died is None:
                    _died = 0
                elif _died == "?":
                    _died = -1
                elif ">" in _died:
                    _died = _died.replace(">", "")
                    _died = int(_died)  # Can we do both statements on same line or will that break?

                # Create newPlayer and add it to the list
                newPlayer = Player(_lastName, _firstName, _fullName, _countries, _born, _died)
                player_list.append(newPlayer)

        return player_list
