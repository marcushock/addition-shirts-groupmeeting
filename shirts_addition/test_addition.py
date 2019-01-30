r""" Example function

This example file has a simple function and documentation.
"""

from addition import add


def test_addition():
    r"""Tests `add(param1, param2)`"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0,0) == 0
