from abc import ABC, abstractmethod
from __future__ import annotations


class Command(ABC):
    """
    The Command Interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccount:
    def __init__(self, balance: int):
        self._balance = balance

    def deposit(self, amount: int):
        self._balance += amount
        print(f"Deposit {amount}. Balance is now {self._balance}")

    def withdraw(self, amount: int):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw {amount}. Balance is now {self._balance}")
        else:
            print(f"Insufficient funds. Balance is {self._balance}")

    def transfer(self, amount: int, recipient: BankAccount):
        if self._balance >= amount:
            self._balance -= amount
            recipient.deposit(amount)
            print(f"Transferred {amount} to recipient. Balance is now {self._balance}")
        else:
            print(f"Insufficient funds. Balance is {self._balance}")


class DepositCommand(Command):
    """
    A concrete command that deposits money into a bank account.
    """

    def __init__(self, account: BankAccount, amount: int):
        self._account = account
        self._amount = amount

    def execute(self):
        self._account.deposit(self._amount)

    def undo(self):
        self._account.withdraw(self._amount)


class WithdrawCommand(Command):
    """
    A concrete command that deposits money into a bank account.
    """

    def __init__(self, account: BankAccount, amount: int):
        self._account = account
        self._amount = amount

    def execute(self):
        self._account.withdraw(self._amount)

    def undo(self):
        self._account.deposit(self._amount)


class TransferCommand(Command):
    def __init__(self, sender: BankAccount, recipient: BankAccount, amount: int):
        self._sender = sender
        self._recipient = recipient
        self._amount = amount

    def execute(self):
        self._sender.transfer(self._amount, self._recipient)

    def undo(self):
        self._recipient.transfer(self._amount, self._sender)


class BankSystem:
    """
    The Invoker class asks the command to carry out the request.
    """

    def __init__(self):
        self._history = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last_command(self):
        if self._history:
            last_command = self._history.pop()
