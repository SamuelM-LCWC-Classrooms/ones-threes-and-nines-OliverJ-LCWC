class Ones_threes_nines:
    def __init__(self, number: int):
        self.ones = number // 1
        self.threes = number // 3
        self.nines = number // 9

n1 = Ones_threes_nines(5)

print(n1.ones)
print(n1.threes)
print(n1.nines)