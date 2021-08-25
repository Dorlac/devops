"""Here is some information on the data model of python."""

# Objects are abstractions for all data
# Obects have three parts, identity, type, and value
#
# Identity
# id(x) returns the address where x is stored
# the "is" operator compares the id's of two objects
#
# Type
# Type defines methods and properties of an object.
# type(x) returns the type that x is
#
# Value
# Value of an object is the only mutable attribute.

# The standard type hierachy
# None is used to specifiy an abject with no value
#
# NonImplemented should be returned when an arithmetic operation has not yet been preformed.
#
# Ellipsis (...) has a single value
#
# Strings are unicode.
#
# Tuple packing is cool. a,b,c = (1,2,3)
#
# Besides Lists, python also has array an dcollections available in extension arrays.
#
# Sets are mutable. Frozen sets are immutable and hashable.
#
# Dictionaries are queues. Keys must be immutable objects.

# Functions
# user defined functions inheret the special attributes from the base function object

# Instance methods
# links a class or class instance to a function
# __self__ represents the class/class_instance and __func__ represents the function.

# Generator functions
# returns an iterator object using the "yield" key word. Calling __iterator__.__next__() is how to
# access the next object in the iterable. Anything with a return statement, a StopIteration
# exception is reaised.

# Coroutine functions
# Defined using "async def". returns a coroutine object. More on this to come.

# Asynchronous generator functions are also a thing.

# Built-in functions
# Just wrappers around C functions. __self__ returns None.

# Built-in methods
# __self__ is set to a python obect which is passed to a built-in function.

# Classes
# Generally, these are factories for class instances. Classes are callable. The arguments of a class
# are passed to __new__() and then typically __init__. Just like most special methods, __new__ can
# be overridden.

# Class instances
# These instance can be made callable by defining __call__() in their class.

# Modules
# Define namespaces with the __dict__ object referenced in functions with __globals__. Other
# attributes include __name__, __file__, and __doc__.

# Custom classes
# Access attributes of class through c.__dict__.["x"] or c.x
# __bases__ is a tuple of parent classes.

# I/O objects (also known as file objects)
# Correlating to the interpreter's standard input, output, and error streams are sys.stdin,
# sys.stdout, and sys.stderr. Abided by the io.TextIOBase abstract class.

# To customize objects: https://docs.python.org/3/reference/datamodel.html

# Context Managers
# Context managers define runtime context and are invoked with the "with" statement.

# Coroutines
# More to come on this in the standard library review.
