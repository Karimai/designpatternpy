It allows the interface of an existing class to be used as another interface.

When we need Adapter design pattern:
* When the class does not have an interface that we need.
* When classes have incompatible interfaces.

It is similar to the Decorator pattern, however it is not designed to be used recursively.

It is an alternative interface over an existing interface. So, it is used when the existing interface does not match the interface required by the client.

It acts as a middleman between two incompatible interfaces, converting the interface of one class into another interface that the client expects.

This pattern is useful when the existing interface is incompatible with the new one which we need. Instead of modifying the existing code, which can be risky and time-consuming, you can create an adapter that translates the existing code's interface into the interface expected by the new system.

