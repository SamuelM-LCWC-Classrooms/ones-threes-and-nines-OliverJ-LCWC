class ones_threes_nines:
    def __init__(self, number: int):
        self.ones = number % 1
        self.fives = number % 5
        self.nines = number % 9
