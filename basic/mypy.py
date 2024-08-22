def add_numbers(a: int, b: int) -> int:
    return a + b


def add_strings(a, b):
    return a + b


if __name__ == "__main__":
    print(add_numbers(1, 2))
    # print(add_strings("a", "b"))
    # print(add_strings("a", 2))


def greeting(name: str) -> str:
    return "Hello, " + name


greeting(42)
