from src.wallet import Wallet

"""
    This would be our first action. 
    Wallet object does not yet exist, but we refer to it as if it is
    Notice that the function's signatures are very explicit 
"""


def test_default_initial_amount():
    """
    Testing initial amount is 0
    """
    wallet = Wallet()
    assert wallet.balance == 0  # Forcing Wallet object to have 'balance' property


def test_setting_initial_amount():
    """
    Testing setter of initial amount
    """
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    """
    Testing adding cash
    """

    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    """
    Testing Spending cash
    """
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

