Behaioral design patterns are design patterns that are concerned with how objects collaborate and communicate with one another to achieve a specific goal.
They provide solutions to common problems that arise when designing systems with objects that interact with one another.

Command design pattern is used to encapsulate a request as an object. thereby allowing for the parameterization of clients with different requests, queue or log requests, and support undoable operations.

Here an abstraction exists between an object that invokes a command and the object that performs the command.

Terminology:
* **Receiver**: The object that will receive and execute the command.
* **Invoker**: The object that sends the command to the Commander.
* **Command**: An object that implements an execute, or action method, and contains all required information to execute it.
* **Client**: The application that is aware of the Receiver, Invoker, and Commands.

It should be undoable. Commands should support undoing their action, allowing the system to rollback changes made by previously executed commands.

Essentially all details of an operation in a separate object.

Define instruction for applying the command.

Undoing the command is optional but recommended.

Composite commands = Macros

We will have an object which represent operations.

