class CoffeeMachine:

    def __init__(self):
        self.on = True
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def get_action(self, action):
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.display_contents()
        elif action == 'exit':
            self.on = False

    def display_contents(self):
        print(f'\nThe coffee machine has:\n'
              f'{self.water} of water\n'
              f'{self.milk} of milk\n'
              f'{self.beans} of coffee beans\n'
              f'{self.cups} of disposable cups\n'
              f'${self.money} of money')

    def take(self):
        print(f'I gave you {self.money}')
        self.money = 0

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:\n'))
        self.milk += int(input('Write how many ml of milk you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.cups += int(input('Write how many disposable coffee cups you want to add:\n'))

    def buy(self):
        print()
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if choice == "back":
            return
        if choice == "1":
            self.change_contents(250, 0, 16, 1, 4)
        elif choice == "2":
            self.change_contents(350, 75, 20, 1, 7)
        elif choice == "3":
            self.change_contents(200, 100, 12, 1, 6)

    def change_contents(self, water_changed, milk_changed, beans_changed, cups_changed, money_changed):
        if self.enough_resources(water_changed, milk_changed, beans_changed):
            self.water -= water_changed
            self.milk -= milk_changed
            self.beans -= beans_changed
            self.cups -= cups_changed
            self.money += money_changed

    def enough_resources(self, water_needed, milk_needed, beans_needed):
        response = 'Sorry, not enough'
        if self.water < water_needed:
            print(f'{response} water!')
            return False
        elif self.milk < milk_needed:
            print(f'{response} milk!')
            return False
        elif self.beans < beans_needed:
            print(f'{response} beans!')
            return False
        elif self.cups <= 0:
            print(f'{response} cups!')
            return False

        print('I have enough resources, making you a coffee!')
        return True


machine = CoffeeMachine()
while machine.on:
    machine.get_action(input('\nWrite action (buy, fill, take, remaining, exit):\n'))
