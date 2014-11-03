"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex -n<=k<0, what is the equivalent index j>=0such that s[j] references
the same element?

>>> l = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
>>> return_element(l, 0)
(2, -20)
>>> return_element(l, 1)
(3, -19)
>>> return_element(l, 2)
(4, -18)
"""


def return_element(data, k):
    """Tells you the equivalent negative index

    Args:
        data (list of int): Simple array
        k (int): index you want to know
        the equivalent negative index

    Returns:
        (val, index)
        val (object): element at position k
        index: negative index of that position
    Examples:
        Here are some examples!

    >>> l = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
    >>> return_element(l, 0)
    (2, -20)
    >>> return_element(l, 1)
    (3, -19)
    >>> return_element(l, 2)
    (4, -18)
    """
    idx = k-len(data)
    return data[idx], idx if data else False