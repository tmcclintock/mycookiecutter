"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import unittest

import pandas

from {{ cookiecutter.project_slug }}.example_module import (
    foo,
    create_random_dataframe
)

"""
Below are two examples of unit tests. The first two tests are
'pytest' style unit tests that utilize fixtures (via a decorator).

Toward the bottom is a 'unittest' (the package) style ``TestCase``
subclass that contains individual unit tests.
"""
@pytest.fixture(params=[1, 42, 500])
def length(request):
    """A parameterized fixture. Each value of the ``params`` list
    is passed one at a time, resulting in three different tests."""
    return request.param


def test_foo():
    """Sample pytest test function."""
    assert foo() == 42


def test_create_random_dataframe(length):
    """Test creating our random dataframe."""
    df = create_random_dataframe(length=length)
    assert len(df) == length
    assert isinstance(df, pandas.DataFrame)


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.lengths = [1, 40, 300]

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_create_random_dataframe(self):
        """Test creating a data frame."""
        for length in self.lengths:
            df = create_random_dataframe(length=length)
            assert len(df) == length
            assert isinstance(df, pandas.DataFrame)
