r""" Example function

This example file has a simple function and documentation.
"""


def add(param1, param2):
    r""" Adds two numbers

    This function adds two numbers

    Parameters
    ----------
    param1 : Union[int, float]
        The first parameter
    param2 : Union[int, float]
        The second parameter

    Returns
    -------
    Union[int, float]
        The sum of `param1` and `param2`

    Example
    -------
    Adding integers:

    >>> add(1, 2)
    3

    Adding floats:
    >>> add(3.7, 1.2)
    4.9

    Using variables:
    >>> a = 1.3
    >>> b = 5
    >>> add(a, b)
    6.3
    """

    return param1 - param2
