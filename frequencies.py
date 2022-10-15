"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    freqs = {}

    for item in list(set(items)): # convert items to set and count each occurrence
        freqs[ele] = test.count(item)

    return frequencies
