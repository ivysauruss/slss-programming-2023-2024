# Functions and Recursion 
# Author: Alissa Xu
# 7 December 2023


import time 

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
    
def fib_itr(n: int) -> int:
    """Returns the nth Fibonacci number. 
    Calculated iteratively."""
    last_num = 0
    num = 1
    result = 1

    for i in range(n - 1):
        result = num + last_num
        
        num, last_num = result, num

    return result
        
    
print(fib(20), fib_itr(20))

time_initial = time.perf_counter()
fib(20)
time_final = time.perf_counter()

print(f"Recursive: {time_final - time_initial}")

time_initial_ = time.perf_counter()
fib_itr(20)
time_final_ = time.perf_counter()

print(f"Iterative: {time_final_ - time_initial_}")