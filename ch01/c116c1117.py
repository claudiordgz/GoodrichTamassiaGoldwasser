__author__ = 'Claudio'

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