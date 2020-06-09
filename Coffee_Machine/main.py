run = True


name = ["water", "milk", "coffee beans", "disposable cups", "money"]
res = [400, 540, 120, 9, 550]
espresso = [250, 0, 16, 1, -4]
latte = [350, 75, 20, 1, -7]
cappuccino = [200, 100, 12, 1, -6]


def printing():
    global res, name
    print("The coffee machine has:")
    for i in range(len(res)):
        print(str(res[i]), "of", name[i])


def buy():
    enough = True
    global res, espresso, name, latte, cappuccino
    what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if what == "1":
        for i in range(len(res)-1):
            if res[i] - espresso[i] < 0:
                print("Sorry not enough", name[i], "!")
                enough = False
                break
        if enough:
            print("I have enough resources, making you a coffee!")
            for i in range(len(res)):
                res[i] -= espresso[i]

    elif what == "2":
        for i in range(len(res) - 1):
            if res[i] - latte[i] < 0:
                print("Sorry not enough", name[i], "!")
                enough = False
                break
        if enough:
            print("I have enough resources, making you a coffee!")
            for i in range(len(res)):
                res[i] -= latte[i]

    elif what == "3":
        for i in range(len(res) - 1):
            if res[i] - cappuccino[i] < 0:
                print("Sorry not enough", name[i], "!")
                enough = False
                break
        if enough:
            print("I have enough resources, making you a coffee!")
            for i in range(len(res)):
                res[i] -= cappuccino[i]
    elif what == "back":
        return


def fill():
    global res
    plus = [0, 0, 0, 0]
    plus[0] = int(input("Write how many ml of water do you want to add:"))
    plus[1] = int(input("Write how many ml of milk do you want to add:"))
    plus[2] = int(input("Write how many grams of coffee beans do you want to add:"))
    plus[3] = int(input("Write how many disposable cups do you want to add:"))

    for i in range(len(plus)):
        res[i] += plus[i]


def take():
    global res
    print("I gave you $", res[4])
    res[4] = 0


def action():
    global run
    act = input("Write action (buy, fill, take, remaining, exit):")

    if act == "buy":
        buy()
    elif act == "fill":
        fill()
    elif act == "take":
        take()
    elif act == "remaining":
        printing()
    elif act == "exit":
        run = False


while run:
    action()