"""
This module contains a basic unit test for the math operations.
Their purposes is to show how to use the pytest framework by example
"""

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