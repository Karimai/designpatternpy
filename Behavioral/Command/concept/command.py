from command_interface import ICommand
from light import Light


class TurnOnCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class TurnOffCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


# Invoder
class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command: TurnOnCommand | TurnOffCommand):
        command.execute()
        self.history.append(command)

    def undo_command(self):
        if self.history:
            command: TurnOnCommand | TurnOffCommand = self.history.pop()
            command.undo()
