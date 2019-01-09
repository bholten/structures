# Basic testing
from src.structures import structure


def test_basic_structures():
    foo = structure(a=1, b=2, c=3, d=4)
    assert foo.a == 1
    assert foo.b == 2
    assert foo.c == 3
    assert foo.d == 4
    assert foo.__slots__ is not None

