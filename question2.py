# -*- coding: utf-8 -*-
"""

@author: Amritesh

Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO

"""
def is_valid_string(test_string):
    char_count = {}
    for char in test_string:
        char_count[char] = char_count.get(char, 0) + 1

    frequencies = list(char_count.values())
    max_freq = max(frequencies)
    min_freq = min(frequencies)

    if frequencies.count(max_freq) == len(frequencies) or frequencies.count(min_freq) == len(frequencies):
        return "YES"

    if frequencies.count(max_freq) == len(frequencies) - 1 and min_freq == 1:
        return "YES"

    if frequencies.count(min_freq) == len(frequencies) - 1 and max_freq - min_freq == 1:
        return "YES"

    return "NO"

# Example usage
s1 = "abc"
print(is_valid_string(s1))  # Output: YES

s2 = "abcc"
print(is_valid_string(s2))  # Output: Yes

s3 = "aabbc"
print(is_valid_string(s3))  # Output: Yes

s4 = "aabbccd"
print(is_valid_string(s4))  # Output: Yes

s5 = "aabbcd"
print(is_valid_string(s5))  # Output: NO

s6 = "aabbccddeefghi"
print(is_valid_string(s6))  # Output: NO

s7 = "xxxaabbccrry"
print(is_valid_string(s7))  # Output: NO

s8 = "abbccc"
print(is_valid_string(s8))  # Output: NO

