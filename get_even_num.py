# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 

@author: Amritesh
"""

def get_even_numbers(numbers):
    '''
    This function returns list of even numbers from a given list

    Parameters
    ----------
    numbers : iterator
        DESCRIPTION.

    Returns
    -------
    list
        list of Even Numbers.

    '''
    
    return [num for num in numbers if num % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
