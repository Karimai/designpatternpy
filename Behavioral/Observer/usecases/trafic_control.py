class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        # firing event
        # When you fire an event, you should send all the parameters
        # that it needs
        self.property_changed("age", value)


class TraficAuthority:
    def __init__(self, person: Person):
        self.person = person
        # register a function as an observer or listener
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Sorry, you still cannot drinve!")
            else:
                print("Okey, you can drive")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":
    p = Person()
    ta = TraficAuthority(p)
    for age in range(14, 19):
        print(f"Setting age to {age}")
        p.age = age
