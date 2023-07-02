# -*- coding: utf-8 -*-
"""
Created on Sun Jul  

@author: Amritesh
"""

from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    """
    Perform a two-sample t-test and return the p-value.

    This function uses the scipy.stats module to calculate the p-value
    for a two-sample t-test between the given sample1 and sample2.

    Parameters:
    sample1 (list): The first sample as a list of numbers.
    sample2 (list): The second sample as a list of numbers.

    Returns:
    float: The p-value resulting from the two-sample t-test.
 
    """
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)