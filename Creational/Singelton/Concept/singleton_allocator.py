import random


class Database:
    initialized = False
    _instance = None

    def __init__(self):
        """
        It is the main problem here. The init function still will be called
        for initialization of every instance.
        """
        print("Generated number: ", random.randint(1, 10))
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


db = Database()

if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(db1 is db2)  # True
