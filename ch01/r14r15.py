""" Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

Give a single command that computes the sum from Exercise R-1.4, relying
on Pythons comprehension syntax and the built-in sum function.

>>> sum_of_squares(10)
285
>>> sum_of_squares(20)
2470
>>> sum_of_squares(500)
41541750
>>> sum_of_squares(37)
16206
>>> sum_of_squares(-1)
False
"""

def sum_of_squares(n):
    """Sum of squares of postive integers
    smaller than n

    Args:
        n (int): Highest number

    >>> sum_of_squares(10)
    285
    >>> sum_of_squares(20)
    2470
    >>> sum_of_squares(500)
    41541750
    >>> sum_of_squares(37)
    16206
    >>> sum_of_squares(-1)
    False
    """
    return sum([pow(x,2) for x in range(n)]) if n > 0 else False
