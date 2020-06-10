from coffeemachine import CoffeeMachine

coffee_machine = CoffeeMachine([400, 150, 75, 10, 500])

while coffee_machine.run:
    coffee_machine.action()
