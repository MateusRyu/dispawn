# dispawn

Discord bot for chess players

## First steps

1. Create virtual environment with `python -m venv env`;
2. Activate virtual environment with `source env/bin/activate`;
3. Install requirements with `pip install -r requirements.txt`;

## How to deactivate a virtual environment

Simply run the following code in the terminal:

```
deactivate
```

## Tests

To execute the tests for the "dispawn" project, you will need to have Python and
pytest installed on your system. If you haven't installed pytest yet, you can do
so via pip:

```bash
pip install pytest
```

Optionally, to generate a code coverage report, you'll need the `pytest-cov`
plugin. You can install it using pip:

```bash
pip install pytest-cov
```

### Run the tests

Once pytest is installed, your can run the tests, once you're in the project
directory and with all dependencies installed, simply execute the following
command to run all the test:

```bash
pytest
```

This command will automatically discover all the teste files (named as `test_*.py`)
in the project directory and its subdirectories (as specified at `pyproject.toml`)
and execute them.

### View test results

After running the tests, pytest will display the results in the terminal. You'll
see a summary of passed (`.`), failed (`F`), expected fail and failed (`x`),
expected fail and don'd fail (`X`) and skipped tests (`s`), along with any error messages
or traceback information for failed tests.

### Tests options

To enhance the test execution and reporting for the "dispawn" project, which is
tested with pytest, you can utilize various CLI options provided by pytest.
Below are explanations and examples of how to use these options:

- **Verbose Output**: For more detailed test results output, use the `-v` (or
  `--verbose`) option. This will show you the name of each test function as they
  are executed;
- **Filtering Tests**: To run tests that match a specific expression, use the
  `-k` option followed by the expression. This allows you to run a subset of tests
  that match certain keywords, like `pytest -k "some_keyword"`;
- **Code Coverage**: To generate a code coverage report, you'll need the
  `pytest-cov` plugin, as said before how to install. Then, you can use the `--cov`
  option to specify which modules to measure coverage for: `pytest --cov=dispawn`.
  Replace `dispawn` with the appropriate module name(s) you wish to generate
  coverage reports for. This command will execute the tests and provide a coverage
  report summarizing how much of the code is covered by tests.
- **Mark Expressions**: pytest allows you to use custom markers to categorize tests.
  After marking tests in your test files, you can run only tests with a specific
  marker using the `-m` option: `pytest --m "mark_name"`. Replace `marker_name` with
  the name of the marker you want to filter tests by. This requires that you have
  previously marked your tests using the `@pytest.mark.marker_name` decorator.
  You can run the tests excluding the marker with `--m "not mark"`:
- **Output Capturing**: By default, pytest captures the output of tests. To see
  the print statements or any other output directly in your console, use the `-s` option.
