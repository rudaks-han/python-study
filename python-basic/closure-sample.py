def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# counter_a = make_counter()
# print(counter_a())  # 1 출력
# print(counter_a())  # 2 출력
#
# counter_b = make_counter()
# print(counter_b())  # 1 출력

def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

# times_two = make_multiplier(2)
# print(times_two(5))  # 10 출력
#
# times_three = make_multiplier(3)
# print(times_three(5))  # 15 출력



def make_account(balance):
    def get_balance():
        return balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance

    return get_balance, deposit, withdraw

get_balance, deposit, withdraw = make_account(100)
print(get_balance())  # 100 출력
print(deposit(50))    # 150 출력
print(withdraw(75))   # 75 출력


def make_power(n):
    return lambda x: x ** n

square = make_power(2)
print(square(5))  # 25 출력

cube = make_power(3)
print(cube(2))    # 8 출력
