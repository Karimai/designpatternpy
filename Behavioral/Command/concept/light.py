from enum import Enum


class Status(Enum):
    ON = "on"
    OFF = "off"


class Light:
    def __init__(self):
        self.status = Status.OFF

    def turn_on(self):
        print("The light is on!")
        self.status = Status.ON

    def turn_off(self):
        print("The light is off!")
        self.status = Status.OFF
