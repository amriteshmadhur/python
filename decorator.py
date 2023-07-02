# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 

@author: Amritesh

"""


import time


def timer(func):
    """
    Decorator that measures the execution time of a function and prints it.
    
    This decorator wraps a function and measures the time taken for the function to execute.
    After the function execution, it prints the execution time in seconds.
    
    Parameters:
    func (function): The function to be decorated.
    
    Returns:
    function: The decorated function.
    
    Example:
    >>> @timer
    ... def my_function():
    ...     # Function code goes here
    ...     time.sleep(2)
    ...
    >>> my_function()
    Execution time: 2.00123 seconds
    """
    
    def decorate_timer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return decorate_timer

@timer
def my_function():
    time.sleep(2)

my_function()



