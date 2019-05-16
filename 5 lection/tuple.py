person = ('George', "Carlin", "May", 12, 1937)

LAST_NAME = 1

BIRTHDAY = slice(2, None)

print(f"Last name: {person[LAST_NAME]}")

print(f"Birthday: {person[BIRTHDAY]}")

# Part 2

from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'age'])

p = Person('Terrence', 'Gilliam', 77)

print('NamedTuple: ', p.first_name, p.last_name, p.age)

p._replace(first_name='Terry')

print('Changed: ', p.first_name, p.last_name, p.age)

print(p[2])

# Part 3

from typing import NamedTuple


class Person(NamedTuple):
    first_name: str
    last_name: str
    age: int = 42


p = Person("Terrence", "Gilliam", 77)

print(p)



