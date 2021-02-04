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
- `python -m pytest --quite` - Gives dots of F if a test fails e.g ....F...
- `python -m pytest --exitfirst or -exit`- Stops after the 1st failure
- `python -m pytest --maxfail` - Gives flexibility on how many tests can fail prior to execution exiting
- `python -m pytest --junit-xml report.xml` - will generate a file called report.xml

#### Configuration Options

[Configuration Files](https://docs.pytest.org/en/latest/customize.html) - should be loaded in the project root directory.

### Chapter 8 - Filtering Tests

You can run tests based on a folder or filter to specific tests

- `python -m pytest tests` - folder level
- `python -m pytest tests/test_accum.py` - folder level and specific test file
- `python -m pytest tests/test_math.py` - specific test files in a folder
- `python -m pytest tests/test_math.py::test_one_plus_one` - specific test case within a file
- `python -m pytest -k one` - will run all tests that contain a certain the substring 'one'
- `python -m pytest -k "one and not accum"` - you and use basic logic to run certain tests, but be careful of false positives

#### Markers and Decorators

To add a marker to test cases, you should use a marker - This can be achieved by:

- `@pytest.mark.math`
- `@pytest.mark.accumulator`

You should also add the custom marker to the pytest configuration file, otherwise you may get warning messages.

```bash
markers =
  accumulator
  math
testpaths = tests
```

Running with selected markers is pretty easy use the following command passing in the marker using -m

- `python -m pytest -m math`

### Chapter 9 Feature Tests

For this chapter we will need to install the requests package, this can be done by running the command
`pip install requests`

Remember to import the requests package `import requests`.  

#### Running The Test

Run the test with this command `python -m pytest -m rest_api`. 

To avoid warnings when running the test, add the markers to the configuration file `pytest.ini`

```bash
markers =
  accumulator
  math
  duckduckgo
  rest_api
```

### Chapter 10 - Extending Pytest With Plugins

#### Reporting Pytest-Html

In an effort to keep track of results, a good idea is to make use of report files.

- [pytest-html](https://github.com/pytest-dev/pytest-html)
- `pip install pytest-html`
- `python -m pytest --html=report.html`

#### Coverage

- `pip install pytest-cov`
- `python -m pytest --cov=stuff` - this would give you the coverage based on the folder `stuff`
- `python -m pytest --cov=stuff --cov-report html` - This will generate an html report for coverage within its own htmlcov folder

The coverage report used here, allows you to click on  files to see where you may have missing coverage.

#### Pytest Xdist

[Pytest Xdist](https://pypi.org/project/pytest-xdist/)

- `pip install pytest-xdist`
- `python -m pytest -n 3` - although for the unit tests it take a bit longer to execute, it would be more beneficial when a greater number of tests are involved

All tests need to be totally independent or you run the risk of collisons

- [A guide to paralell testing](https://automationpanda.com/2018/01/21/to-infinity-and-beyond-a-guide-to-parallel-testing/)

#### Pytest BDD

- [Pytest BDD](https://pypi.org/project/pytest-bdd/)