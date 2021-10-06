import csv

from Classes.Player import Player


class Csv_Reader:
    def __init__(self):
        pass

    def read_file(self, _fileName):
        # Open CSV List

        player_list = []

        with open(_fileName, "r", encoding="utf8") as csv_file:
            # Init a csv Module reader object passing the csv_file into the object
            reader = csv.reader(csv_file)
            # Skip 1 line (Header)
            next(reader, None)
            # Row Unpacking begins
            for _lastName, _firstName, _fullName, _countries, _born, _died in reader:
                # We need to parse _countries into a list, countries is a Quotes string each country seperated by comma

                country_list = []
                # Not Gate Logic here (Inverse)
                if "," not in _countries:
                    country_list.append(_countries)
                # Triggers when multiple countries detected
                else:
                    multi_Countries = _countries.split(',')
                    for country in multi_Countries:
                        country_list.append(country)

                # Process the various conditions of the file

                _bornID = None

                if _born == "?":
                    _bornID = 0
                elif "<" in _born:
                    _bornID = _born.replace("<", "")
                    _bornID = int(_bornID)  # Can we do both statements on same line or will that break?
                else:
                    _bornID = _born

                deathID = None
                if _died is None:
                    deathID = 0
                elif _died == "?":
                    deathID = -1
                elif ">" in _died:
                    deathID = _died.replace(">", "")
                    deathID = int(deathID)  # Can we do both statements on same line or will that break?
                else:
                    deathID = _died

                newPlayer = Player(_lastName, _firstName, _fullName, _countries, _bornID, deathID)
                player_list.append(newPlayer)

        return player_list
