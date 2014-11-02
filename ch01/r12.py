"""Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators

>>> is_even(127)
False
"""


def is_even(k):
    """Return True if n is even
    Else returns False

    >>> is_even(10)
    True
    >>> is_even(9)
    False
    >>> is_even(11)
    False
    >>> is_even(13)
    False
    >>> is_even(1025)
    False
    >>> is_even("test")
    Number must be Integer values
    """
    try:
        return int(k) & 1 == 0
    except ValueError:
        print("Numbers must be Integer values")

if __name__ == "__main__":
    import doctest
    doctest.testmod()