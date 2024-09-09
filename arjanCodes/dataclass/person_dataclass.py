import json
from dataclasses import dataclass, field, asdict
from typing import List


@dataclass(order=True)
class Person:
    name: str
    age: int = 20


@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)  # 빈 리스트를 기본값으로 설정


if __name__ == "__main__":
    # person = Person(name="John", age=30)
    # person2 = Person(name="John", age=30)
    # print(person)  # Person(name=John, age=30)
    # print(repr(person))
    # print(str(person))
    # print(person == person2)

    # team1 = Team("Developers")
    # team1.members.append("Alice")
    # print(team1)  # 출력: Team(name='Developers', members=['Alice'])

    # person1 = Person("Bob", 20)
    # person2 = Person("Bob", 25)
    # print(person1 < person2)

    person = Person("Alice", 30)
    person_json = json.dumps(asdict(person))
    print(person_json)  # 출력: {"name": "Alice", "age": 30}
    pass
