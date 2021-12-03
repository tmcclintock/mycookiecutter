"""Example source code for `{{ cookiecutter.project_slug }}`"""

import numpy
import pandas


def foo() -> int:
    """Returns the number 42."""
    return 42


def create_random_dataframe(length: int) -> pandas.DataFrame:
    """
    Create a dataframe of length ``length`` with four columns of
    junk data in it with names ``A``, ``B``, ``C`` and ``D``.

    Args:
        length (int): length of the output dataframe

    Returns:
        a dataframe with random data in it
    """
    return pandas.DataFrame(numpy.random.randn(length, 4), columns=list("ABCD"))