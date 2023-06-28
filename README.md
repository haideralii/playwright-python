# Requirements

  * Python 3.7
  * Playwright

## Install the Pytest plugin:

```
pip install pytest-playwright
```

## Install the required browsers:

```
playwright install
```

## Install the required python pacakges and plugins:

```
pip install -r requirements.txt
```

## To execute tests

create .env file and copy contents of .env.example file into .env file

## Sample Execution

run following command to execute all tests

```
pytest
```

run following command to execute single test by test name

```
pytest -k "test_name_of_test"
```

Running tests in headed mode

```
pytest --headed 
```

Running Tests on specific browsers

```
pytest --browser webkit
```

Test Generator

```
playwright codegen demo.playwright.dev/todomvc
```

Emulate devices

```
pytest --device="iPhone 11"
```

For more documentation go to playwright and pytest official sites

https://playwright.dev/python/docs/intro

https://docs.pytest.org/en/7.2.x/
