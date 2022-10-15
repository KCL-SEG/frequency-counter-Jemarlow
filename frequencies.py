"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    frequencies = {}

    for item in list(set(items)): # convert items to set and count each occurrence
        frequencies[item] = items.count(item)

    return frequencies
