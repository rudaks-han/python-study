from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


def main() -> None:
    person = Person(name="John", age=30)
    print(person.name)
    print(person.age)
    person.name = "Jane"
    person.age = 25
    print(person.name)
    print(person.age)


if __name__ == "__main__":
    main()
