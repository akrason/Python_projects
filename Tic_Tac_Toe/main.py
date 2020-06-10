# write your code here
x = input("Enter cells: ")

matrixt = [[x[i * 3], x[i * 3 + 1], x[i * 3 + 2]] for i in range(3)]


def matrix():
    print("---------")
    for i in range(3):
        print("| {} {} {} |".format(matrixt[i][0], matrixt[i][1], matrixt[i][2]))

    print("---------")


def printing(value):
    if value == 1:
        print("Game not finished")
    elif value == 2:
        print("Draw")
    elif value == 3:
        print("X wins")
    elif value == 4:
        print("O wins")
    elif value == 5:
        print("Impossible")


def check():
    nx, no, win = 0, 0, 0
    for p in range(len(x)):
        if x[p] == "X":
            nx += 1
        elif x[p] == "O":
            no += 1
    if abs(no - nx) > 1:
        return 5

    # checking in row
    for inx in range(3):
        if matrixt[inx][0] == matrixt[inx][1] == matrixt[inx][2]:
            win += 1
            m = matrixt[inx][0]
        elif matrixt[0][inx] == matrixt[1][inx] == matrixt[2][inx]:
            win += 1
            m = matrixt[0][inx]
        if win > 1:
            return 5

    # checking diagonals
    if x[0] == x[4] == x[8]:
        win += 1
        m = x[4]
    elif x[2] == x[4] == x[6]:
        win += 1
        m = x[4]

    if win > 1:  # impossible
        return 5
    elif win == 0:
        if (no + nx) == 9:  # no empty fields
            return 2
        else:
            return 1
    else:
        if m == "O":
            return 4
        else:
            return 3


matrix()
printing(check())
