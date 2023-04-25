import random

from service_interface import IService


class ServiceProtectionProxy(IService):
    def __init__(self):
        print("initialized successfully")

    def request(self):
        auth = [True, False][random.randint(0, 1)]
        if auth:
            return "Welcome, let's go!"
        else:
            return "Authentication failed. Try again"
