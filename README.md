# Requirements

  * Python 3.7
  * Playwright
  * Docker Installed (if to execute tests on docker)

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

To create the docker image of playwright python, execute following command and it will take sometime

```
docker build -t playwright_python .
```

To execute tests on docker container, execute following command

```
docker run -it --env-file .env  playwright_python
```

Also you can use following command as well

```
docker compose up
```

After executing tests to view HTML report, excute following command, just replance container_id with your container_id on which teste executed

```
docker cp conatiner_id:/app/report.html ./report.html
```

For more documentation go to playwright and pytest official sites

https://playwright.dev/python/docs/intro

https://docs.pytest.org/en/7.2.x/
