"""What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?

>>> range_from_fifty()
[50, 60, 70, 80]
"""
def range_from_fifty():
    """ Creates a list
    with values 50, 60, 70, 80

     Returns:
        list: [50, 60, 70, 80]

    >>> range_from_fifty()
    [50, 60, 70, 80]
    """
    return range(50,81,10)