from service_interface import IService


class Service(IService):
    def __init__(self):
        self.data = {1: "one", 2: "two"}

    def request(self):
        print(self.data)
