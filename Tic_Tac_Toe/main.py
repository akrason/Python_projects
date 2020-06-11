# write your code here
import sys
from game import Game

game = Game()


def new(sign):
    cord = input("Enter the coordinates: ").split()
    x = cord[0]
    y = cord[1]
    if x.isdigit() and y.isdigit():
        y = int(y)
        x = int(x)
        if x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
            new(sign)
        elif game.table[x-1][y-1] != " ":
            print("This cell is occupied! Choose another one!")
            new(sign)
        else:
            game.update(x, y, sign)
            
    else:
        print("You should enter numbers!")
        new(sign)


def printing(value):
    if value == 1:
        pass
    elif value == 2:
        print("Draw")
        sys.exit()
    elif value == 3:
        print("X wins")
        sys.exit()
    elif value == 4:
        print("O wins")
        sys.exit()


def check():
    win = 0
    global count
    count += 1
    # checking in row
    for inx in range(3):
        if game.table[inx][0] == game.table[inx][1] == game.table[inx][2]:
            if game.table[inx][0] != " ":
                win = 1
                m = game.table[inx][0]
        elif game.table[0][inx] == game.table[1][inx] == game.table[2][inx]:
            if game.table[0][inx] != " ":
                win = 1
                m = game.table[0][inx]

    if game.table[1][1] != " ":
        if game.table[0][0] == game.table[1][1] == game.table[2][2]:
            win = 1
            m = game.table[1][1]
        elif game.table[2][0] == game.table[1][1] == game.table[0][2]:
            win = 1
            m = game.table[1][1]
    if win == 1:
        if m == "O":
            return 4
        else:
            return 3
    elif count == 9:
        return 2
    else:
        return 1


print(game)
count = 0
checks = 0
value = 1

while value == 1:
    if count % 2 == 0:
        sign = "X"
    else:
        sign = "O"
    new(sign)
    value = check()
    print(game)
    printing(value)


