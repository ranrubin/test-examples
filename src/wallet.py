

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    """
    This Object represent a wallet
    """

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        """
        imitates spending money from wallet
        :param amount: Integer, amount to reduce from balance
        """
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        """
        Imitates adding cash to wallet
        :param amount: Integer, amount to add to wallet

        """
        self.balance += amount

