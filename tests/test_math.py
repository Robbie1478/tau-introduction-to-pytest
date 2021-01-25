"""
This module contains a basic unit test for the math operations.
Their purposes is to show how to use the pytest framework by example
"""

import pytest

#----------------------
# A basic test function
#----------------------

def test_one_plus_one():
    assert 1 + 1 == 2

#Left this intentionally failing as an example

def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)