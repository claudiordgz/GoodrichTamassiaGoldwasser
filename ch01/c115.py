__author__ = 'Claudio'


""" Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
def check_if_unique(data):
    s = set(data)
    return len(s) == len(data)

