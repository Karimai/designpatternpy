The OOP concepts used here:
1. Abstraction: The `command` interface defines the `execute` and `undo` methods that all concrete commands must implement. This abstraction allows the invoker (`RemoteControl`) to work with commands in a generic way, without knowing the specific details of each command.
2. Encapsulation: Each concrete command encapsulates a request (such as `turn_on` or `turn_off`) as an object. along with any necessary data, such as the receiver object (`Light`).
3. Polymorphism: The `RemoteControl` class can execute any object that implements the `Command` interface, allowing for polymorphic behavior.
4. Separation of concepts: The `Light` class is responsible for implementing the functionality of turning the light on ot off, while the `Command` classes are responsible for encapsulating these actions into objects.
5. Loose coupling: The invoker (`RemoteControl`) is decoupled from the receiver (`Light`) and the concrete commands, as it only knows about the `Command` interface.

Command Design Pattern Terminologies:
1. **Receiver**: The object that performs the action associated with the command; `Light` class in this example.
2. **Command**: The object that encapsulates a request as an object, allowing for parameterization of clients with different requests.
3. **Concrete Command**: A specific implementation of the `Command` interface that encapsulates a particular action.
4. **Invoker**: The object that receives commands and executes them; `RemoteControl`.
5. **Client**: The object that creates commands and passes them to the invoker.

