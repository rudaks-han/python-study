class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance

    @property
    def balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount


def main() -> None:
    account = BankAccount(100)
    account.withdraw(50)
    account.deposit(100)
    print(account.balance)


if __name__ == "__main__":
    main()