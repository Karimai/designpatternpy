The main idea comes from the fact that complicated objects are not created from scratch.

The Prototype pattern allows you to create copies of an existing object, known as a prototype, instead of creating new objects from scratch. This can be useful :
1. when the creation of an object is time-consuming of resource-intensive
2. expensive
3. or you need to create objects that are similar but not identical.

Instead of creating a new object every time, you can create a prototype object and clone it whenever you need a new instance.

Overall, the prototype pattern provides a way to avoid creating new objects from scratch by allowing you to clone existing objects with updated attributes. Usefule when creating an object is expensive or time-consuming.

An existing design is the Prototype.

Some benefits:
* A Prototype is created from an object that is already instantiated. Imagine using the existing object as the class template to create a new object, rather than calling a specific class.
* The ability to create a Prototype means that you don't need to create many classes for specific combinations of objects. You can create on object, that has a specific configuration, and then clone this version many times, rather than creating a new object from a predefined class definition.
* New Prototypes can be created at runtime, without knowing what kind of attributes the protorype may eventually have. For example, you have a sophisticated object that was randomly created from many factors. and you want to clone it rather than re applying all the same functions over and over again.

To implement Prototype Desing Pattern, you should create fully or partially an object, then copy them for a new object and change the attribute for the new object.
