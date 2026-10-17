# python_qa

A learning project in test automation with Python: API, database and UI tests (pytest, Playwright, Allure).

## Requirements

- Python 3.13
- Poetry

## Installation

Clone the repository:

```
git clone https://github.com/exiledkid/python_qa.git
cd python_qa
```

Install dependencies:

```
poetry install
```

Install the browser for UI tests:

```
poetry run playwright install chromium
```

## Running tests

Run all tests:

```
poetry run pytest tests
```

Run UI tests with a visible browser:

```
poetry run pytest tests/test_ui_checkout.py --headed
```