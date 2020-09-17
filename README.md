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
- Separation of concerns is a major key to understandable code; many design concepts arise directly from this principle
- Functions extract named concepts from procedural code. Clarity and separation are the primary objectives of extraction; reuse is a secondary benefit.
- Classes group closely related behaviors and data together into an object
- Modules group related classes, functions, and data while keeping independent concerns separate. Explicitly importing code from other modules makes it clear what's being used where.
- Packages help create a hierarchy of modules that helps with naming and code discovery.

## Errata and questions

If you find an error in the code or the book, or if you have a question about the content, please read the [contribution guidelines](.github/CONTRIBUTING.md) to understand the best course of action.
The errata are published on [the book's homepage](https://bit.ly/the-python-pro).
