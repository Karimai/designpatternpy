class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, receiver, message):
        self.room.message(self.name, receiver, message)


class ChatRoom:
    """
    This is a mediator pattern.
    """

    def __init__(self):
        self.people = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person):
        join_msg = f"{person.name} join the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)
                break


if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(jane)
    room.join(john)

    john.say("Hi room")
    jane.say("oh, hey John")

    simon = Person("Simon")
    room.join(simon)

    simon.say("Hello everybody!")

    jane.private_message("Simon", "Glad you join!")
