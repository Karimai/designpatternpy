from abc import ABC


class LightState(ABC):
    current_state: str = None

    def show_status(self):
        pass

    def perform_action(self):
        pass


class RedLightState(LightState):
    current_state = "Red"

    def show_status(self):
        print("Traffic light is Red.")

    def perform_action(self):
        print("Allow the traffic to proceed.")


class YellowLightState(LightState):
    current_state = "Yellow"

    def show_status(self):
        print("Traffic light is Yellow")

    def perform_action(self):
        print("Prepare to change the signal.")


class GreenLightState(LightState):
    current_state = "Green"

    def show_status(self):
        print("Traffic light is Green!")

    def perform_action(self):
        print("Allow traffic to proceed.")


class TrafficLight:
    def __init__(self):
        self.state = RedLightState()
        self.previous_state = ""

    def change_state(self):
        current_state = self.state.current_state
        if self.state.current_state == "Yellow":
            if self.previous_state == "Red":
                self.state = GreenLightState()
            if self.previous_state == "Green":
                self.state = RedLightState()
        else:
            self.state = YellowLightState()
        self.previous_state = current_state

    def show_state_info(self):
        self.state.show_status()

    def perform_action(self):
        self.state.perform_action()


traffic_light = TrafficLight()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
traffic_light.change_state()
traffic_light.show_state_info()
