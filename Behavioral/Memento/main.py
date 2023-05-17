class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def create_memento(self):
        return Memento(self._state)


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []

    def save_state(self, originator: Originator):
        memento = originator.create_memento()
        self._mementos.append(memento)

    def restore_state(self, originator: Originator):
        if self._mementos:
            memento = self._mementos.pop()
            state = memento.get_state()
            originator.set_state(state)


origin = Originator()
care_taker = Caretaker()

origin.set_state("State 1")
print("Current state: ", origin.get_state())

care_taker.save_state(origin)

origin.set_state("State 2")
print("Current state:", origin.get_state())

origin.set_state("State 3")
print("Current state:", origin.get_state())

care_taker.restore_state(origin)
print("Restored state:", origin.get_state())
