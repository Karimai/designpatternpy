import copy


class Address:
    def __init__(self, street: str, country: str, city: str, number: int):
        self.country = country
        self.city = city
        self.street = street
        self.number = number

    def __str__(self):
        return f"{self.number}, {self.street}, {self.city}, {self.country}"

class Person:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("De Helf", "England", "London", 8))
print(john)

jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.number = 10
print(jane)
