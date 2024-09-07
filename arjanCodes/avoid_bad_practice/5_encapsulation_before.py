class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance


def main() -> None:
    account = BankAccount(100)
    account.balance -= 150
    account.balance += 100
    print(account.balance)


if __name__ == "__main__":
    main()
