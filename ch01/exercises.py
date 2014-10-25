__author__ = 'Claudio'

import collections

""" Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""
def is_multiple(n, m):
    return True if (n % m == 0) else False

"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators
"""
def is_even(k):
    return (k & 1 == 0)

""" Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
class MinMax():
    def __init__(self, field1, field2):
        self.min = field1
        self.max = field2
    def __str__(self):
        return "Min {min} - Max {max}".format(min=str(self.min), max=str(self.max))
def minmax(data):
    start = 0
    mm = MinMax(data[start],data[start])
    if len(data) & 1  == 1:
        if data[start] < data[start+1]:
            mm.max = data[start+1]
            mm.min = data[start]
            start += 2
        else:
            start += 1
    for index in [x*2 for x in range(len(data[start:])/2)[1:]]:
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
    print(is_multiple(50,3))
    print(is_multiple(60,3))
    print(is_multiple(70,3))
    print(is_multiple(50,2))
    print(is_multiple(60,2))
    print(is_multiple(70,2))
    print(is_even(10))
    print(is_even(9))
    print(is_even(11))
    print(is_even(13))
    l = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
    print(minmax(l))