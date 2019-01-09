# A somewhat perfomant implementation of C-style structures.
# Abuses the __slots__ attribute to gain some extra performance.


class Struct(object):
    """Simple Struct class.

    Accepts arbitrary keywords arguments and then assigns them to its internal __dict__ attribute.
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def structure(**kwargs):
    """Creates and instance of Struct and then loads its attributes into the internal __slots__ field."""
    struc = Struct(**kwargs)
    struc.__slots__ = kwargs.keys()
    return struc
