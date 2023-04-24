class Target:
    """
    The target defines the domain-specific interface used by the client.
    """

    def request(self, order: str) -> str:
        return order


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code.
    """

    def reverse_request(self, order: str) -> str:
        return order[::-1]


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self, order: str) -> str:
        return f"Adapter {self.adaptee.reverse_request(order)}"


if __name__ == "__main__":
    numbers = "1 2 3 4 5"
    print(f"I can go forward: {numbers}")
    print("target can also go forward: ", end="")
    target = Target()
    print(target.request(numbers))

    adaptee = Adaptee()
    print("Adaptee can go backward: ", end="")
    print(f"{adaptee.reverse_request('1 2 3 4 5')}")

    print(
        "Adapter has the interface of the Target,"
        " but it needs the functionality of Adaptee"
    )
    adapter = Adapter(adaptee)
    print(adapter.request("1 2 3 4 5"))
