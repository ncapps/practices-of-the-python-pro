# Exercises for Practices of the Python Pro 🐍📘

<img src="cover.png" width="500" alt="Practices of the Python Pro, a Manning book by Dane Hillard">

This repository contains the source code for the examples and exercises contained in [Practices of the Python Pro](https://bit.ly/the-python-pro).
The repository is a template repository, so if you'd like to follow along with the book you can [make your own copy](https://github.com/daneah/practices-of-the-python-pro/generate).

Each chapter's examples are in their own directory.
In some chapters, you'll find multiple snippets in a single module.
These won't always produce output when you run them, and are occasionally meant only as snippets to demonstrate a concept.
In later chapters, some modules act as an entrypoint to run a program from the command line, importing other modules along the way.
Follow along in the book for more context!

## Notes
### Ch 2. Separation of concerns
- When a class depends on another class, those classes are said to be coupled. If a class depends on many details of another class, such that changing one requires changing the other, those classes are tightly coupled.
- We want our classes to have high cohesion because if everything in a class is closely related, our concerns are likely to be well separated. When a class’s methods and attributes are closely related, it is said to have high cohesion.
- The process of breaking a problem into small, manageable pieces is called decomposition.
- If a function becomes too long or does too many things, it can be difficult to characterize and therefore difficult to name.
- Clear code requires you to keep less knowledge in your head at any given time
- Separation of concerns is a major key to understandable code; many design concepts arise directly from this principle
- Functions extract named concepts from procedural code. Clarity and separation are the primary objectives of extraction; reuse is a secondary benefit.
- Classes group closely related behaviors and data together into an object
- Modules group related classes, functions, and data while keeping independent concerns separate. Explicitly importing code from other modules makes it clear what's being used where.
- Packages help create a hierarchy of modules that helps with naming and code discovery.

### Ch 3. Abstraction and encapsulation
- Abstraction is a tool for deferring obligatory comprehension of code.
- Abstraction takes many forms: decomposition, encapsulation, programming style, and inheritance versus composition.
    - Decomposition is the separation of something into its constituent components
    - Encapsulation groups related functions and data into a larger construct.
    - Programming styles: procedural, functional, declarative
    - Composition frees you from the limitations of a hierarchy while still providing the concept of relatedness between two things
- Each approach to abstraction is useful, but context and extent of use are important considerations.
- Refactoring is an iterative process; abstraction that once worked may need to be revisited later.

### Ch 4. Designing for high performance
- Design for performance both up front and iteratively throughout your development.
- *Time complexity* is a measure of how quickly your code can perform a task in relation to its inputs
- *Space complexity* is a measure of how your code uses disk space or memory as its inputs grow.
- The ideal complexity is constant time (O(1)), which doesn’t depend on the size of the inputs
- It’s useful to examine the worst case to get a better sense for what the code is capable of. Big O notation always measures the worst-case complexity of code for this reason.
- Think carefully about the right data type for the task.
- Prefer generators over lists when you don’t need all the values at once, to save on memory usage.
- Use the timeit and cProfile/profile Python modules to test your hypotheses about complexity and performance.

### Ch 5. Testing your software
- Functional tests make sure code produces the expected output from a given input.
- Testing saves you time in the long run by catching bugs and making refactoring code easier.
- Manual testing isn’t scalable and should be used to supplement automated testing.
- Unittest and pytest are two popular unit and integration testing frameworks for Python.
- Test-driven development puts the tests first, guiding you to a working implementation based on the requirements.

### Ch 6. Separation of concerns in practice
- Separation of concerns is a tool for achieving more readable, maintainable code.
- End-user applications are often separated into persistence, business logic, and presentation layers.
- Separation of concerns works closely with encapsulation, abstraction, and loose coupling.
- Applying effective separation of concerns allows you to add, change, and delete functionality without affecting the surrounding code.

### Ch 7. Extensibility and flexibility
- Code is said to be *extensible* if adding new behaviors to it has little or no impact on existing behaviors.
- The mapping of choices to messages acts like configuration—information a program uses to determine how to execute. Configuration is often easier to understand than conditional logic.
- Deep nesting is a strong hint that concerns need further separation.
- if/elif/else are difficult to reason about
- *Inversion of control* says that instead of creating instances of dependencies in your class, you can pass in existing instances for the class to make use of. The control of dependency creation is inverted by giving the control to whatever code is creating.
- Making testing easier is one of the big reasons to follow the principles you’ve learned in this book. If your code is hard to test, it may be hard to understand as well. If it’s easy to test, it may be easy to understand. Neither is certain, but they’re correlated.
- This practice of sharing agreed-upon interfaces (in contrast with class-specific details) between high- and low-level code will give you the freedom to swap implementations in and out.
- *Entropy* is the tendency for organization to dissolve into disorganization over time. Code often starts out small, neat, and understandable, but it tends toward complexity over time.
- Build code so that adding new features means adding new functions, methods, or classes without editing existing ones.
- Inversion of control allows other code to customize behavior to its needs without changing the low-level implementation.
- Sharing agreed-upon interfaces between classes instead of giving them detailed knowledge about each other reduces coupling.
- Be deliberate about what input types you want to handle, and be strict about your output types.

### Ch 8. The rules (and exceptions) of inheritance
- _Parent_ classes are referred to as superclasses in Python (and in many other languages). Child classes are referred to as subclasses.
- A class inherits all of its superclass’s information and behavior, and it can then override them to do something different. This is probably the tightest coupling that exists in programming. A class is fully coupled to its superclass because everything it knows and does by default is tied to that superclass.
- Inheritance is for specialization of behavior.
- Ideal use case for inheritance
    1. Shallow, narrow hierarchy: makes it easer to reason about. Narrow means there shouldn't be too many subclasses.
    2. Subclasses are at the leaves of the object graph; they don't make use of other objects. If a subclass has a unique dependency that the superclass or any other subclasses don’t have, composition might be a better way to accomplish that portion of the task.
    3. Subclasses use (or specialize) all the behavior of their superclass
- The latest versions of Python support type hinting, which is a way to tell developers and automated tooling what types of objects a function or method expects
- Python also supports the idea of multiple inheritance, where a subclass may have two or more direct superclasses
- You can see the method resolution order for any class by using its __mro__ attribute:
- Abstract base classes in Python are a way of using something that looks like inheritance to achieve something that’s effectively an interface. An abstract base class, like a formal interface in other languages, outlines which methods and attributes its subclasses must implement. Python provides the abc module for easing the creation of abstract base classes
- Use inheritance to represent true is-a relationships (good for specialization of behavior).
- Use composition for has-a relationships (good for reuse of code).
- Method resolution order is key to keeping multiple inheritance straight.
- Abstract base classes provide interface-like control and safety in Python.

## Errata and questions

If you find an error in the code or the book, or if you have a question about the content, please read the [contribution guidelines](.github/CONTRIBUTING.md) to understand the best course of action.
The errata are published on [the book's homepage](https://bit.ly/the-python-pro).
