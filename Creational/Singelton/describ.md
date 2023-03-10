The Singleton can be accessible globally, but it is not a global variable. It is a class that can be instanced at any time, but after it is first instanced, any new instances will point to the same instances as the first.

Important note:
* For a class to behave as a Singleton, it should not contain any references to `self` but use static variables, static methods and/or class methods.
* This implementation is not thread-safe. If multiple threads try to create the instance of the class simultaneously, it's possible that more than one instance will be created. To make this implementation thread-safe, a lock or a synchronized block should be used to ensure than only one thread can create the instance at a time.
Notes:
`cls` is a reference to the class
`self` is a reference to an instance of the class
`__new__` is the constructor. A static method which create the class
`__init__` is the initializer. A normal method which initialize the instance variables



By returning a reference to cls in the `__new__`, we force the class to act as a singleton. For a class to act as a singleton, it should not contain any references to self.
