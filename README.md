# tau-introduction-to-pytest

- [Web UI Python Path](https://testautomationu.applitools.com/learningpaths.html?id=web-ui-python-path)  
- [Introduction To Pytest with Andrew Knight](https://testautomationu.applitools.com/pytest-tutorial/)

## Requirements for this course

- [Python can be downloaded from here](https://www.python.org/downloads/)
- [Python documentation can be found here](https://docs.pytest.org/en/stable/)

### Chapter 1 - The First Test Case

#### Running a Test

```bash
Notice that both our test module and our test function contain the prefix "test_". 

When pytest runs, it will discover tests from its current directory down. 
By default, any function names with the prefix "test_" in any modules with the prefix "test_" 
will be identified and executed as test cases.
```

You can run test from the command line using `python -m pytest.`

### Chapter 2 - A Failin Test Case

#### A Failing Test

The following will fail with an assertion error.

```bash
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c
```

### Chapter 3 - A Test With An Exception

Exception from 1 test won't affect other tests.

To handle dision by zero, we can `import pytest` and handle it with `assert 'divison by zero' in str(e.value)`

```bash
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)
```

### Chapter 4 - Paramtrized Test Cases

Using tuples in products can help reduce code, especially repeated code when used with the parametrize function

```bash
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
```

To furter extend this, you could check out `Hypothesis`, which is a testing library which can integrate wiht `pytest`.

### Chapter 6 - Fixtures

- [Python Generators](https://realpython.com/introduction-to-python-generators/)

[Python Fixtures](https://docs.pytest.org/en/stable/fixture.html) are special functions the pytest can call before test case functions.  
Using Python Fixtures means you can make use of the [DRY - Don't Repeat Yourself Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) thus reducing repeated code and allows for passing in the return value into the test case funtion.  
This is also known as [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) in Python.

#### Sharing Fixtures Across Test Modules

To share fixture across test modules - create a file called `conftest.py` with the `tests` folder, ensuring you remember the imports.
A test case can use multiple fixtures, just ensure each fixture has a unique name.

```bash
import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()
```

### Chapter 7 - Commands and Configs

#### Command Console Output

- `python -m pytest --help`
- `python -m pytest` - runs all tests
- `python -m pytest --verbose or -v` - pytest prints more data, enables you to see more data at a glance
- `python -m pytest --quite` - Gives dots of F if a test fails
- `python -m pytest --exitfirst or -exit`- Stops after the 1st failure
- `python -m pytest --maxfail` - Gives flexibility on how many tests can fail prior to execution exiting
- `python -m pytest --junit-xml report.xml` - will generate a file called report.xml

#### Configuration Options

[Configuration Files](https://docs.pytest.org/en/latest/customize.html) - should be loaded in the project root directory.
