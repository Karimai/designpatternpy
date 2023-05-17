class Mediator:
    def __init__(self):
        self.colleagues = []

    def set_colleague(self, colleague):
        self.colleagues.append(colleague)

    def send(self, message, colleague):
        if colleague == self.colleagues[0]:
            self.colleagues[1].notify(message)
        elif colleague == self.colleagues[1]:
            self.colleagues[0].notify(message)


class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        pass


class ConcreteColleague1(Colleague):
    def notify(self, message):
        print("ConcreteColleague1 received:", message)


class ConcreteColleague2(Colleague):
    def notify(self, message):
        print("ConcreteColleague2 received:", message)


mediator = Mediator()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)

mediator.set_colleague(colleague1)
mediator.set_colleague(colleague2)

colleague1.send("Hello from colleague 1!")
colleague2.send("Hello from colleague 2!")
