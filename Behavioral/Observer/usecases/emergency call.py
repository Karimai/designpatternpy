class Event(list):
    def __call__(self, *args, **kwargs):
        for observer in self:
            observer(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        # Now call the event!
        # fire the event!
        # firing event function sends two argument, so the observers should get two parameters
        self.falls_ill(name=self.name, addr=self.address)


def call_doctor(**kwargs):
    print(f"{kwargs['name']} needs a docker at {kwargs['addr']}")


if __name__ == "__main__":
    person = Person("Ali", "Shahed 12")

    person.falls_ill.append(lambda **kwargs: print(f"{kwargs['name']} is ill"))

    person.falls_ill.append(call_doctor)

    person.catch_a_cold()

    person.falls_ill.remove(call_doctor)

    person.catch_a_cold()
