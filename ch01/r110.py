""" What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?

>>> range_from_eigth()
[8, 6, 4, 2, 0, -2, -4, -6, -8]
"""

def range_from_eigth():
    """ Return the list [8, 6, 4, 2, 0, -2, -4, -6, -8]
    :return:
        the list [8, 6, 4, 2, 0, -2, -4, -6, -8]
    >>> range_from_eigth()
    [8, 6, 4, 2, 0, -2, -4, -6, -8]
    """
    return range(8, -9, -2)
