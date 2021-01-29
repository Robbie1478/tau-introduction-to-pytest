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

#-------------------------------------
# A Parameterised Test Function
#-------------------------------------

products = [
    (2, 3, 6),                  # two positive integers
    (1, 99, 99),                # identity: multiplying any number by 1
    (0, 99, 0),                 # zero: multiply any number by 1
    (3, -4, -12),               # positive by a negative
    (-5, -5, 25),               # negative by a negative
    (2.5, 6.7, 16.75)           # mutliply floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product



