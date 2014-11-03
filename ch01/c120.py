__author__ = 'Claudio'

"""Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""
def sub_shuffle(data, indexlist):
    import random
    index = random.randint(0, len(indexlist)-1)
    rElement = data[indexlist[index]]
    indexlist.pop(index)
    return rElement

def custome_shuffle(data):
    indexes_of_data = range(len(data))
    return [sub_shuffle(data, indexes_of_data) for e in range(len(data))]