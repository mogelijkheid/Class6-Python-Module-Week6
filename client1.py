import random

class Client:

   
    def __init__(self, name, total_amount):
        self.name = name
        self.total_amount = total_amount
        self.account_number = random.randint(10000,99999)


    def withdraw(self, amount):
        if amount > self.total_amount:
            print("Not enough money!")
        else:
            self.total_amount -= amount
            print(f'The sum of {amount} has been withdrawn from your account balance.')
            return self.balance()

    def deposit(self, amount):
        self.total_amount += amount
        print(f'The sum of {amount} has been added to your account balance.')
        return self.balance()

    def balance(self):
        print(f'Your current account balance is: {self.total_amount}')
        return self.total_amount


