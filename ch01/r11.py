"""Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

>>> is_multiple(50,3)
False
"""

def is_multiple(n, m):
    """Return True if n is multiple of m such that n = mi
    Else returns False

    >>> is_multiple(50,3)
    False
    >>> is_multiple(60,3)
    True
    >>> is_multiple(70,3)
    False
    >>> is_multiple(-50,2)
    True
    >>> is_multiple(-60,2)
    True
    >>> is_multiple("test",10)
    Numbers must be Integer values
    >>> is_multiple(-60,"test")
    Numbers must be Integer values
    """
    try:
        return True if (int(n) % int(m) == 0) else False
    except ValueError:
        print("Numbers must be Integer values")

if __name__ == "__main__":
    import doctest
    doctest.testmod()