- - -
### Design patterns:
__Design patterns__ are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

Design patterns differ by their complexity, level of detail and scale of applicability to the entire system being designed. I like the analogy to road construction: you can make an intersection safer by either installing some traffic lights or building an entire multi-level interchange with underground passages for pedestrians.

Patterns are devided into three main groups:
- __Creational patterns__ provide object creation mechanisms that increase flexibility and reuse of existing code.
- __Structural patterns__ explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.
- __Behavioral patterns__ take care of effective communication and the assignment of responsibilities between objects.
- - -
### Creational Patterns
1. __Abstract Factory__ is a creational design pattern that lets you produce families of related objects without specifying their concrete classes:
![abstract_factory](/images/design_patterns/abstract_factory.png)
Link -> https://refactoring.guru/design-patterns/abstract-factory
2. __Builder__ is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code:
![builder](/images/design_patterns/builder.png)
Link -> https://refactoring.guru/design-patterns/builder
3. __Factory Method__ is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created:
![factory](/images/design_patterns/factory.png)
Link -> https://refactoring.guru/design-patterns/factory-method
4. __Prototype__ is a creational design pattern that lets you copy existing objects without making your code dependent on their classes:
![prototype](/images/design_patterns/prototype.png)

Link -> https://refactoring.guru/design-patterns/prototype
5. __Singleton__ is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance
![singleton](/images/design_patterns/singleton.png)

Link -> https://refactoring.guru/design-patterns/singleton
- - -
### Structural Patterns
1. __Adapter__ is a structural design pattern that allows objects with incompatible interfaces to collaborate:
![adapter](/images/design_patterns/adapter.png)
Link -> https://refactoring.guru/design-patterns/adapter
2. __Bridge__ is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other:
![bridge](/images/design_patterns/bridge.png)
Link -> https://refactoring.guru/design-patterns/bridge
3. __Composite__ is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects:
![composite](/images/design_patterns/composite.png)
Link -> https://refactoring.guru/design-patterns/composite
4. __Decorator__ is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors:
![decorator](/images/design_patterns/decorator.png)
Link -> https://refactoring.guru/design-patterns/decorator
5. __Facade__ is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes (A facade can become __a god object__ coupled to all classes of an app):
![facade](/images/design_patterns/facade.png)
Link -> https://refactoring.guru/design-patterns/facade
6. __Flyweight__ is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object:
![flyweight](/images/design_patterns/flyweight.png)
Link -> https://refactoring.guru/design-patterns/flyweight
7. __Proxy__ is a structural design pattern that lets you provide a substitute or placeholder for another object:
![proxy](/images/design_patterns/proxy.png)
Link -> https://refactoring.guru/design-patterns/proxy
- - -
### Behavioral Patterns
1. __Chain of Responsibility__ is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain:
![chain_of_responsibility](/images/design_patterns/chain_of_responsibility.png)
Link -> https://refactoring.guru/design-patterns/chain-of-responsibility
2. __Iterator__ is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.):
![iterator](/images/design_patterns/iterator.png)
Link -> https://refactoring.guru/design-patterns/iterator
3. __Memento__ is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation:
![memento](/images/design_patterns/memento.png)
Link -> https://refactoring.guru/design-patterns/memento
4. __State__ is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class:
![state](/images/design_patterns/state.png)
Link -> https://refactoring.guru/design-patterns/state
- - -
### Useful links
- https://refactoring.guru/design-patterns/python
- - -