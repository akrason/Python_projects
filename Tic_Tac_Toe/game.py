class Game:
    def __init__(self):
        self.table = [[" ", " ", " "] for i in range (3)]

    def __str__(self):
        return '---------\n| {} |\n| {} |\n| {} |\n---------'.format(
            ' '.join(self.table[0]),
            ' '.join(self.table[1]),
            ' '.join(self.table[2]))

    def update(self, x, y, sign):
        self.table[x-1][y-1] = sign

