""" Python's random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parametrization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.

>>> data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
>>> results = list()
>>> for x in range(len(data)*20):
...     val = custom_choice(data)
...     results.append(val in data)
>>> print(results)
[True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True, \
True, True, True, True, True, True, True, True, True, True]
"""

def custom_choice(data):
    import random
    return data[random.randrange(0,len(data))]