import json
from icecream import ic


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"str Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"repr Person(name={self.name}, age={self.age})"


if __name__ == "__main__":
    person = Person(name="John", age=30)
    person2 = Person(name="John", age=30)
    ic(person)  # Person(name=John, age=30)
    ic(repr(person))
    ic(str(person))
    ic(person == person2)
