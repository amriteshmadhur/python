# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:27:04 2023

@author: 0002J0744
"""

def calculate_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float or None: The mean value of the numbers. Returns None if the input list is empty.

    Example:
    >>> data = [10, 15, 20, 25, 30]
    >>> mean_value = calculate_mean(data)
    >>> print("Mean:", mean_value)
    Mean: 20.0
    """
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)