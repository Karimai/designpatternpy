The main goal is to decouple an abstraction from its implementation. This pattern is useful when you want to create a set of orthogonal classes where each class has its own independent functionality, and it is possible to mix and match any implementation with any abstraction.

The difference between Adapter pattern and Bridge pattern is the intention of the development.

The Bridge pattern is for refactoring the code, while the Adapter pattern creates an interface on top of an existing code without refactoring the code.

The Bridge design pattern is used to separate abstraction from implementation. It allows the client to work with different implementations of an abstraction without knowing the implementation details. It decouples an abstraction from its implementation so that they can vary independently.

Use when you want to separate a solution where the abstraction and implementation may be tightly coupled, and you want to break it up into smaller conceptual parts.

When there is a bridge abstraction, it is possible to extend each side separately without breaking the other.

