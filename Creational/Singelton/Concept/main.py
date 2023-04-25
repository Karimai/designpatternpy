import copy


class Singleton:
    """
    The Singleton class
    """

    "Variables declared at class level are static variables that can be accessed"
    " directly using the class name without needing the class to be instantiated"
    value = []

    def __new__(cls, *args, **kwargs):
        """
        You can come here and modify how the object is constructed.
        It returns a reference to itself.
        """
        return cls

    @staticmethod
    def static_mtd():
        """
        Use @staticmethod if no inner variables required.
        """

    @classmethod
    def class_method(cls):
        """
        Use @classmethod to access class level variables or methods
        """
        print(cls.value)


# The client
# All clients point out to the same memory address (id)

print(f"id of Singleton Class: \t {id(Singleton)}")

Obj1 = Singleton()
print(f"id of Singleton Obj1: \t {id(Obj1)}")

Obj2 = copy.deepcopy(Obj1)
print(f"id of Singleton Obj2 \t {id(Obj2)}")
