from command import RemoteControl, TurnOffCommand, TurnOnCommand
from light import Light

if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()
    turn_on = TurnOnCommand(light=light)
    turn_off = TurnOffCommand(light=light)

    remote.execute_command(turn_on)
    remote.execute_command(turn_off)
    remote.undo_command()
    remote.undo_command()
