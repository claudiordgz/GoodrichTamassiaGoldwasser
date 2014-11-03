""" Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

>>> print(minmax([2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]))
Min 1 - Max 11
"""

class MinMax():
    """MinMax object helper

    Attributes:
        min (int): Minimun value of attributes
        max (max): Maximum value of attributes

    """
    def __init__(self, min, max):
        """Args:
          min (int): Number with lesser value
          max (int): Number with higher value
      """
        self.min = min
        self.max = max
    def __str__(self):
        """String representation overload
        """
        return "Min {min} - " \
               "Max {max}".format(min=str(self.min),
                                  max=str(self.max))

def minmax(data):
    """This is the algorithm to find the
    minimum and maximun in a list.

    Args:
        data (list of int): Simple array of
        Integers

    Returns:
        A tuple MinMax that holds the minimum
        and maximum values found in the list

    Examples:
        Here are some examples!

    >>> print(minmax([2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]))
    Min 1 - Max 11
    >>> print(minmax([50,200,300,3,78,19203,56]))
    Min 3 - Max 19203
    >>> print(minmax([100,150,200,500]))
    Min 100 - Max 500
    """
    start = 0
    mm = MinMax(data[start],data[start])
    if len(data) & 1  == 1:
        if data[start] < data[start+1]:
            mm.max = data[start+1]
            mm.min = data[start]
            start += 2
        else:
            start += 1
    for index in range(start, len(data[start:]), 2):
        if data[index] < data[index+1] :
            l_min = data[index]
            l_max = data[index+1]
        else:
            l_min = data[index+1]
            l_max = data[index]
        if mm.min > l_min:
            mm.min = l_min
        if mm.max < l_max:
            mm.max = l_max
    return mm

if __name__ == "__main__":
    import doctest
    doctest.testmod()