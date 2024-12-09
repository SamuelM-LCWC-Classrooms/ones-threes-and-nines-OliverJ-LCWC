class Ones_threes_nines:
    def __init__(self, number: int):
        self.ones = number % 1
        self.threes = number % 3
        self.nines = number % 9
