# Functions and REcursion 
# Author: Alissa Xu
# 7 December 2023

def factorial(n: int) -> int:
    """Return the nth factorial.
    Done recursively.
    
    Example: 
        factorial(3) -> 3! -> 6
    """

    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return factorial(n-1) * n
    

print(factorial(4))

def fib(n: int) -> int:
    """Return the nth Fibonacci number. C
    Calculated recursively. """
    if n in [1, 2]: 
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
    
print(fib(20))

