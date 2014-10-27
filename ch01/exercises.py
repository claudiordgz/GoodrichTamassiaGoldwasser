# coding=utf-8
__author__ = 'Claudio'


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

"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
"""Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""
def sum_of_squares(n):
    return sum([pow(x,2) for x in range(n)]) if n > 0 else False

"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
""" Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""
def sum_of_odd_squares(n):
    return sum([pow(x,2) for x in range(1, n, 2)]) if n > 0 else False

"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n≤k<0, what is the equivalent index j ≥0such that s[j] references
the same element?
"""
def return_element(data, k):
    idx = k-len(data)
    return data[idx], idx if data else False

"""What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
def range_from_fifty():
    return range(50,81,10)

""" What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""
def range_from_eigth():
    return range(8, -9, -2)

"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
def list_comprehension_example():
    return [pow(2,x) for x in range(9)]

""" Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
def custom_choice(data):
    import random
    return data[random.randrange(0,len(data))]

"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""
def custom_reverse(data):
    return [data[len(data)-x-1] for x in range(len(data))]

""" Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
def get_odd_numbers(data):
    return [k for k in data if (k & 1 == 1)]

""" Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
def check_if_unique(data):
    s = set(data)
    return len(s) == len(data)

""" In our implementation of thescale function (page 25), the body of the loop
executes the command data[j] = factor. Wehave discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""
""" Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val = factor
Explain why or why not.
"""
"""
MutableNum class from: http://blog.edwards-research.com/2013/09/mutable-numeric-types-in-python/

Allows you to pass the instance to a function, and with proper coding, allows you to modify the
value of the instance inside the function and have the modifications persist.

For example, consider:

>   def foo(x): x *= 2
>   x = 5
>   foo(x)
>   print(x)

This will print 5, not 10 like you may have hoped.  Now using the MutableNum class:

>   def foo(x): x *= 2
>   x = MutableNum(5)
>   foo(x)
>   print(x)

This *will* print 10, as the modifications you made to x inside of the function foo will persist.

Note, however, that the following *will not* work:

>   def bar(x): x = x * 2
>   x = MutableNum(5)
>   bar(x)
>   print(x)

The difference being that [x *= 2] modifies the current variable x, while [x = x * 2] creates a new
variable x and assigns the result of the multiplication to it.

If, for some reason you can't use the compound operators ( +=, -=, *=, etc.), you can do something
like the following:

>   def better(x):
>       t = x
>       t = t * 2
>       # ... (Some operations on t) ...
>
>       # End your function with a call to x.set()
>       x.set(t)

"""
class MutableNum(object):
    __val__ = None
    def __init__(self, v): self.__val__ = v
    # Comparison Methods
    def __eq__(self, x):        return self.__val__ == x
    def __ne__(self, x):        return self.__val__ != x
    def __lt__(self, x):        return self.__val__ <  x
    def __gt__(self, x):        return self.__val__ >  x
    def __le__(self, x):        return self.__val__ <= x
    def __ge__(self, x):        return self.__val__ >= x
    def __cmp__(self, x):       return 0 if self.__val__ == x else 1 if self.__val__ > 0 else -1
    # Unary Ops
    def __pos__(self):          return self.__class__(+self.__val__)
    def __neg__(self):          return self.__class__(-self.__val__)
    def __abs__(self):          return self.__class__(abs(self.__val__))
    # Bitwise Unary Ops
    def __invert__(self):       return self.__class__(~self.__val__)
    # Arithmetic Binary Ops
    def __add__(self, x):       return self.__class__(self.__val__ + x)
    def __sub__(self, x):       return self.__class__(self.__val__ - x)
    def __mul__(self, x):       return self.__class__(self.__val__ * x)
    def __div__(self, x):       return self.__class__(self.__val__ / x)
    def __mod__(self, x):       return self.__class__(self.__val__ % x)
    def __pow__(self, x):       return self.__class__(self.__val__ ** x)
    def __floordiv__(self, x):  return self.__class__(self.__val__ // x)
    def __divmod__(self, x):    return self.__class__(divmod(self.__val__, x))
    def __truediv__(self, x):   return self.__class__(self.__val__.__truediv__(x))
    # Reflected Arithmetic Binary Ops
    def __radd__(self, x):      return self.__class__(x + self.__val__)
    def __rsub__(self, x):      return self.__class__(x - self.__val__)
    def __rmul__(self, x):      return self.__class__(x * self.__val__)
    def __rdiv__(self, x):      return self.__class__(x / self.__val__)
    def __rmod__(self, x):      return self.__class__(x % self.__val__)
    def __rpow__(self, x):      return self.__class__(x ** self.__val__)
    def __rfloordiv__(self, x): return self.__class__(x // self.__val__)
    def __rdivmod__(self, x):   return self.__class__(divmod(x, self.__val__))
    def __rtruediv__(self, x):  return self.__class__(x.__truediv__(self.__val__))
    # Bitwise Binary Ops
    def __and__(self, x):       return self.__class__(self.__val__ & x)
    def __or__(self, x):        return self.__class__(self.__val__ | x)
    def __xor__(self, x):       return self.__class__(self.__val__ ^ x)
    def __lshift__(self, x):    return self.__class__(self.__val__ << x)
    def __rshift__(self, x):    return self.__class__(self.__val__ >> x)
    # Reflected Bitwise Binary Ops
    def __rand__(self, x):      return self.__class__(x & self.__val__)
    def __ror__(self, x):       return self.__class__(x | self.__val__)
    def __rxor__(self, x):      return self.__class__(x ^ self.__val__)
    def __rlshift__(self, x):   return self.__class__(x << self.__val__)
    def __rrshift__(self, x):   return self.__class__(x >> self.__val__)
    # Compound Assignment
    def __iadd__(self, x):      self.__val__ += x; return self
    def __isub__(self, x):      self.__val__ -= x; return self
    def __imul__(self, x):      self.__val__ *= x; return self
    def __idiv__(self, x):      self.__val__ /= x; return self
    def __imod__(self, x):      self.__val__ %= x; return self
    def __ipow__(self, x):      self.__val__ **= x; return self
    # Casts
    def __nonzero__(self):      return self.__val__ != 0
    def __int__(self):          return self.__val__.__int__()               # XXX
    def __float__(self):        return self.__val__.__float__()             # XXX
    def __long__(self):         return self.__val__.__long__()              # XXX
    # Conversions
    def __oct__(self):          return self.__val__.__oct__()               # XXX
    def __hex__(self):          return self.__val__.__hex__()               # XXX
    def __str__(self):          return self.__val__.__str__()               # XXX
    # Random Ops
    def __index__(self):        return self.__val__.__index__()             # XXX
    def __trunc__(self):        return self.__val__.__trunc__()             # XXX
    def __coerce__(self, x):    return self.__val__.__coerce__(x)
    # Represenation
    def __repr__(self):         return "%s(%d)" % (self.__class__.__name__, self.__val__)
    # Define innertype, a function that returns the type of the inner value self.__val__
    def innertype(self):        return type(self.__val__)
    # Define set, a function that you can use to set the value of the instance
    def set(self, x):
        if   isinstance(x, (int, long, float)): self.__val__ = x
        elif isinstance(x, self.__class__): self.__val__ = x.__val__
        else: raise TypeError("expected a numeric type")
    # Pass anything else along to self.__val__
    def __getattr__(self, attr):
        print("getattr: " + attr)
        return getattr(self.__val__, attr)

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data

"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""
def demonstration_list_comprehension():
    return [idx*x for idx, x in enumerate(range(1,11))]

"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""
def demonstration_list_comprehension_abc():
    return [chr(x) for x in range(ord('a'), ord('z')+1)]

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

"""Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""
def read_sdin(data):
    age = 1
    if age > 0:
        try:
            age = int(input( "Enter other person's age:" ))
            data.append(age)
            if age <= 0:
                print( "Your age must be positive" )
            read_sdin()
        except ValueError:
            print( "That is an invalid age specification" )
            read_sdin()
        except EOFError:
            print(data)
            print( "There was an unexpected error reading input." )
            raise
    else:
        read_sdin()


"""Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product ofa and b. That is, it returns
an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.
"""


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
    print(sum_of_squares(10))
    print(sum_of_squares(20))
    print(sum_of_squares(500))
    print(sum_of_squares(37))
    print(sum_of_squares(-1))
    print(sum_of_odd_squares(10))
    print(sum_of_odd_squares(20))
    print(sum_of_odd_squares(500))
    print(sum_of_odd_squares(37))
    print(sum_of_odd_squares(-1))
    print(return_element(l, 0))
    print(return_element(l, 1))
    print(return_element(l, 2))
    print(range_from_fifty())
    print(range_from_eigth())
    print(list_comprehension_example())
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_reverse(l))
    print(get_odd_numbers(l))
    print(check_if_unique(l))
    print(check_if_unique(l[:7]))
    l2 = [MutableNum(x) for x in l]
    print(scale(l2, 5))
    print(demonstration_list_comprehension())
    print(demonstration_list_comprehension_abc())
    print(custome_shuffle(l))
    s = list()
    read_sdin(s)