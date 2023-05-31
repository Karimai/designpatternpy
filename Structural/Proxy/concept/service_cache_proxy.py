from service import Service
from service_interface import IService


class ServiceCacheProxy(IService):
    def __init__(self):
        self.data = {}
        self.service = Service()

    def request(self):
        if len(self.data) == 0:
            print("let initialize it.")
            self.data = self.service.data
        return self.data
