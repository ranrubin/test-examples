from src.wallet import Wallet


def main():
    wallet = Wallet(70)
    wallet.add_cash(4)

    wallet = Wallet("ran")
    wallet.add_cash(4)


if __name__ == '__main__':
    main()