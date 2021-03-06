"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python's comprehension syntax and the built-in sum function.

"""

def sum_of_odd_squares(n):
    """Sum of squares of odd postive integers
    smaller than n

    Args:
        n (int): Highest number

    >>> sum_of_odd_squares(10)
    165
    >>> sum_of_odd_squares(20)
    1330
    >>> sum_of_odd_squares(500)
    20833250
    >>> sum_of_odd_squares(37)
    7770
    >>> sum_of_odd_squares(-1)
    False
    """
    return sum([pow(x,2) for x in range(1, n, 2)]) if n > 0 else False