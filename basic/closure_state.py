def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter_a = make_counter()
print(counter_a())  # 1 출력
print(counter_a())  # 2 출력

counter_b = make_counter()
print(counter_b())  # 1 출력
