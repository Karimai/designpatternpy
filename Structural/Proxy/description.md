Wrapping functionality around something (objects, classes)

Or create an additional layer of abstraction.

A virtual proxy can cache elements of a real subject before loading the full object into memory.

A protection proxy can provide an authentication layer.

Difference between proxy and Adapter: The Adapter will try to adapt two existing interfaces together. Here the interfaces are the same.

A proxy object acts as an intermediary between a client and the real object, controlling access to the real object and providing additional functionality if needed.

In essence, the Proxy Design Pattern allows you to substitute an object with another object that can perform additional tasks such as lazy **initialization**, **caching**, **logging**, or **authentication**.
