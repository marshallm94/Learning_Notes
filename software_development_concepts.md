# What is CI/CD and how does it work?

Check out [this article](https://semaphoreci.com/blog/cicd-pipeline)

# Python

## Namespaces, `import` & `__init__.py` files

## Exception Handling

General exception handling structure is as follows:

```python
try:
    # main logic goes here
except ExceptionOrErrorType1 as e:
    # logic for when ExceptionOrErrorType1 occurs in the try block
except ExceptionOrErrorType2 as e:
    # logic for when ExceptionOrErrorType2 occurs in the try block
#...
except ExceptionOrErrorTypeN as e:
    # logic for when ExceptionOrErrorTypeN occurs in the try block
else:
    # logic for when no exception/error occurs in the try block
finally:
    # logic that runs *no matter what* 
```

There are a few nuances with the `finally` block:
* From [the documentation](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions): "**the finally
  clause will execute as the last task before the try statement completes**. The finally clause runs whether or not the
  try statement produces an exception."
* From [the documentation](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions): "In real world
  applications, **the finally clause is useful for releasing external resources (such as files or network connections),
  regardless of whether the use of the resource was successful**."

* There can be as many `except ExceptionOrErrorTypeN` clausees as you would like

## Packages, Namespaces, `import` & `__init__.py` files


* [The import system](https://docs.python.org/3/reference/import.html#regular-packages)
* [Packing Python Projects](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)
* [Packages](https://docs.python.org/3/tutorial/modules.html#packages)


Python has only one type of module object, and all modules are of this type, regardless of whether the module is
implemented in Python, C, or something else. To help organize modules and provide a naming hierarchy, Python has a
concept of packages.

* Packages

    * Conceptual:
        * Packages are the "top" of the hierarchy or the outermost circle in a set of concentric cirlces representing
          packages, subpackages, modules.

```
meta_package/
└── package
    ├── __init__.py
    ├── module_A.py
    ├── module_B.py
    ├── module_C.py
    └── sub_package
        ├── __init__.py
        ├── module_D.py
        ├── module_E.py
        └── module_F.py

2 directories, 8 files
```
