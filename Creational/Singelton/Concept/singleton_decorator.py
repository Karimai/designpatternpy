import random


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        """
        This function will be called only one time!
        """
        print("Loading database ", random.randint(1, 100))


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 is d2)  # True
