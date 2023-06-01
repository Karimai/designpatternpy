from __future__ import annotations

from abc import ABC


class State(ABC):
    def on(self, switch: Switch):
        print("The light is already on!")

    def off(self, switch: Switch):
        print("The light is already off!")


class OnState(State):
    def __init__(self):
        print("the light is turning on!")

    def off(self, switch: Switch):
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("The light is turning off!")

    def on(self, switch: Switch):
        switch.state = OnState()


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


if __name__ == "__main__":
    sw = Switch()
    sw.on()
    sw.off()
