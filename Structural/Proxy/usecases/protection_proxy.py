class Driver:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"Car being driven by {self.driver.name}")


class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print(f"Driver ({self.driver.name}) is too young!")


if __name__ == "__main__":
    car = CarProxy(Driver("Karim", 41))
    car.drive()

    car = CarProxy(Driver("Ramtin", 15))
    car.drive()
