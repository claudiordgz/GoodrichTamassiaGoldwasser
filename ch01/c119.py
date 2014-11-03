__author__ = 'Claudio'

"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""
def demonstration_list_comprehension_abc():
    return [chr(x) for x in range(ord('a'), ord('z')+1)]