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
