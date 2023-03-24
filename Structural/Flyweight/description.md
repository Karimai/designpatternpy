The Flyweight pattern is a memory optimization pattern by sharing some immutable states.

Intrinsic (Immutable, Shared) state: The attributes which are not change between instances.
Extrinsic (unique) state: The attributes which are specific to a given instances and can not be shared with other instances.

Cons: 
* Need to use the Factory Design by itself. Design pattern inside design pattern.
* Complex to understand.
* Trap for premature optimisation.

Useful when dealing with large numbers of objects that have similar or identical intrinsic state.

