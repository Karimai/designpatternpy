class Person:
    def __init__(self):
        print("Creating an instance of Person")
        # address
        self.address = None
        self.postcode = None
        self.city = None
        # info
        self.company = None
        self.position = None
        self.income = None

    def __str__(self) -> str:
        return f"Address: {self.address, self.postcode, self.city}\n" \
               f"Employee at {self.company} as a {self.position} earning {self.income}\n"


class PersonBuilder:  # Facade
    def __init__(self, person: Person = None):
        self.person = Person() if person is None else person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company = company
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, income):
        self.person.income = income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, address):
        self.person.address = address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    p = pb.\
        works.at("Fynch").as_a("Developer").earning(2000).\
        lives.at("Ganzeril").with_postcode("6721 RK").in_city("Bennekom").\
        build()
    print(p)
