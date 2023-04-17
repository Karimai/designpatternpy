import copy


class Address:
    def __init__(self, street: str, suite: int, city: str):
        self.street = street
        self.suite = suite
        self.city = city

    def __str__(self):
        return f"{self.street}, {self.city}, Suite: #{self.suite}"


class Employee:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("124 East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto: Employee, name: str, suite: int):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


jane = EmployeeFactory.new_main_office_employee("Jane", 123)
john = EmployeeFactory.new_aux_office_employee("John", 234)

print(john, "\n", jane)
