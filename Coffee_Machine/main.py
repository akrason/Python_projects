from coffeemachine import CoffeeMachine


def main(args):
    coffee_machine = CoffeeMachine([400, 150, 75, 10, 500])

    while coffee_machine.run:
        coffee_machine.action()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))