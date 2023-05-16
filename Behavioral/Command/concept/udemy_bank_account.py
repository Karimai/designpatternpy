from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:
    OVERDRAFTLIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance is {self.balance}")
        return True

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFTLIMIT:
            self.balance -= amount
            print(f"Withdraw {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action: Action, amount: int):
        self.success = None
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount()
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)

    cmd.invoke()
    print(f"After $100 deposit: {ba}")
    cmd.undo()
    print(f"After undo, deposit: {ba}")

    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print(f"Withdraw too much: {ba}")
    illegal_cmd.undo()
    print(f"after undo: ")
