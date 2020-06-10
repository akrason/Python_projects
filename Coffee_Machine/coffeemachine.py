class CoffeeMachine(object):

    def __init__(self, res):
        # names of products
        self.name = ["water", "milk", "coffee beans", "disposable cups", "money"]
        # how many resources machine has
        self.res = res
        # cost of individual types of coffee
        self.espresso = [250, 0, 16, 1, -4]
        self.latte = [350, 75, 20, 1, -7]
        self.cappuccino = [200, 100, 12, 1, -6]
        self.enough = True
        self.run = True

    def printing(self):
        print("The coffee machine has:")
        for i in range(len(self.res)):
            print(str(self.res[i]), "of", self.name[i])

    def buy(self):
        self.enough = True
        what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if what == "1":
            for i in range(len(self.res) - 1):
                if self.res[i] - self.espresso[i] < 0:
                    print("Sorry not enough", self.name[i], "!")
                    self.enough = False
                    break
            if self.enough:
                print("I have enough resources, making you a coffee!")
                for i in range(len(self.res)):
                    self.res[i] -= self.espresso[i]
        elif what == "2":
            for i in range(len(self.res) - 1):
                if self.res[i] - self.latte[i] < 0:
                    print("Sorry not enough", self.name[i], "!")
                    self.enough = False
                    break
            if self.enough:
                print("I have enough resources, making you a coffee!")
                for i in range(len(self.res)):
                    self.res[i] -= self.latte[i]
        elif what == "3":
            for i in range(len(self.res) - 1):
                if self.res[i] - self.cappuccino[i] < 0:
                    print("Sorry not enough", self.name[i], "!")
                    self.enough = False
                    break
            if self.enough:
                print("I have enough resources, making you a coffee!")
                for i in range(len(self.res)):
                    self.res[i] -= self.cappuccino[i]
        elif what == "back":
            return

    def printing(self):
        print("The coffee machine has:")
        for i in range(len(self.res)):
            print(str(self.res[i]), "of", self.name[i])

    # adding resources to coffee machine
    def fill(self):
        plus = [0, 0, 0, 0]
        plus[0] = int(input("Write how many ml of water do you want to add:"))
        plus[1] = int(input("Write how many ml of milk do you want to add:"))
        plus[2] = int(input("Write how many grams of coffee beans do you want to add:"))
        plus[3] = int(input("Write how many disposable cups do you want to add:"))

        for i in range(len(plus)):
            self.res[i] += plus[i]

    # taking money from coffee machine
    def take(self):
        print("I gave you $", self.res[4])
        self.res[4] = 0

    def action(self):
        act = input("Write action (buy, fill, take, remaining, exit):")

        if act == "buy":
            self.buy()
        elif act == "fill":
            self.fill()
        elif act == "take":
            self.take()
        elif act == "remaining":
            self.printing()
        elif act == "exit":
            self.run = False
            pass
