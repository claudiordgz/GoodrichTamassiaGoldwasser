__author__ = 'Claudio'


"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""
def demonstration_list_comprehension():
    return [idx*x for idx, x in enumerate(range(1,11))]
