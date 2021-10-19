# Recursion


**Linear Recursive Process**
* A linear recursive process is one that has **one** base condition/references itself **once**.
* Example: 

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

**Tree-Recursive Process**
* A tree-recursive process is one that has **more than one** base condition/references itself **more than once**
* Example:

```python
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
```

This process can be represented with the following structure:

![](images/recursive_fibonacci.png)


**Question to self (2021-08-31)**:
* Is the number of base conditions/axioms **always** equal to the number of times the procedure references itself in the
  function/procedure definition?
