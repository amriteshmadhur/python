# -*- coding: utf-8 -*-
"""

@author: Amritesh
"""

def get_frequency(string):
    word_list = string.split() 
    word_count = {}  

    # Count the frequency of each word
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1

    max_frequency = max(word_count.values())

    # Find the length of the highest-frequency word
    highest_frequency_word = [word for word, freq in word_count.items() if freq == max_frequency]
    length = len(highest_frequency_word[0])

    return length


# Example usage
string = "write write write all the number from from from 1 to 100"
print(get_frequency(string))  # Output: 5
