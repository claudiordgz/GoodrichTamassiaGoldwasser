"""Demonstrate how to use Python's list
comprehension syntax to produce the list
[1, 2, 4, 8, 16, 32, 64, 128, 256].

>>> list_comprehension_example()
[1, 2, 4, 8, 16, 32, 64, 128, 256]
"""
def list_comprehension_example():
    """ Return list
    [1, 2, 4, 8, 16, 32, 64, 128, 256]

    :return:
        list: [1, 2, 4, 8, 16, 32, 64, 128, 256]

    >>> list_comprehension_example()
    [1, 2, 4, 8, 16, 32, 64, 128, 256]
    """
    return [pow(2,x) for x in range(9)]

