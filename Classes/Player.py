class Player:
    def __init__(self, _lastName, _firstName, _fullName, _Countries, _born, _died):
        self.lastName = _lastName
        self.firstName = _firstName
        self.fullName = _fullName
        self.countries = _Countries  # a List, Most of the time only containing one element
        self.born = _born
        self.died = _died  # Optional, Default None. If 0 Then player is alive. Elif -1(?) Died but year not known.
        # else Spit out died. This will be a
        # function

    def __str__(self):
        return f"DEBUGGING LASTNAME: {self.lastName}. Player Name {self.fullName} was born in the year {self.birth()} and has represented {self.countries}. {self.firstName}{self.living()}."

    # I don't like returning dynamic type but this is python I guess
    def birth(self):
        if self.born == -1:
            return "unknown"
        else:
            return f"{self.born}"

    def living(self):
        if self.died == "":
            return " is still alive"
        elif self.died == -1:
            return " died in an unknown year"
        else:
            return f" died in year {self.died}"
