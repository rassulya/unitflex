# UnitFlex: Python Package Assignment

## Objective

Create a modular Python package called `unitflex` that performs unit conversions between multiple domains. Your implementation must follow the structure below and pass the provided test suite. The package should be installable and buildable using the `uv` tool.

## Requirements

### Functionality

Your package must provide a function:

```python
def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float
```

This function handles conversion between units in a given domain. You must implement conversion logic for the following domains:

* Temperature:

  * `celsius` to `fahrenheit`
  * `fahrenheit` to `celsius`
* Distance:

  * `kilometers` to `miles`
  * `miles` to `kilometers`
* Currency:

  * `usd` to `eur`
  * `eur` to `usd`
  * You may use either fixed conversion rates or live exchange rate lookup (see optional section below)

Invalid domains or units must raise a `ValueError`.

### Project Structure

Use the following project structure:

```
unitflex/
├── unitflex/
│   ├── __init__.py
│   ├── core.py            # contains convert()
│   ├── temperature.py     # temperature logic
│   ├── distance.py        # distance logic
│   ├── currency.py        # currency logic
├── cli.py                 # optional CLI entry point
├── pyproject.toml         # for building with uv
├── tests/                 # provided by instructor
│   ├── test_core.py
│   ├── test_temperature.py
│   ├── test_distance.py
│   ├── test_currency.py
```

You may not change the names of the files or folder layout.

### Building and Installation

Use `uv` to manage your environment and build your package.

1. Create the environment and install in editable mode:

```
uv venv
uv pip install -e .
```

2. Run the test suite:

```
uv add pytest
pytest
```

3. Build the package:

```
uv build
```

The `.whl` and `.tar.gz` files should appear in the `dist/` directory.

### Implementation Guidelines

* Each domain (`temperature`, `distance`, `currency`) must be implemented in a separate module.
* The `core.py` file should import from the domain modules and dispatch to the correct logic based on the `domain` argument.
* Do not use any external libraries unless explicitly allowed.
* Only the standard library is permitted.

## Tests You Must Pass

Your implementation must pass all tests in the `tests/` folder. These tests are provided by the instructor in [repo](https://github.com/rassulya/unitflex) and cover:

* Correct results for all supported conversions
* Proper exception raising for unsupported domains or units
* Edge cases (e.g., negative temperatures, high values)
* Independence of domain logic
* CLI behavior (if implemented)

You will not submit your own tests. 

## Optional Features (Bonus)

### Command-Line Interface

Implement a command-line interface in `cli.py` that accepts arguments:

```
python cli.py <domain> <from_unit> <to_unit> <value>
```

Example:

```
python cli.py temperature celsius fahrenheit 100
```

This should call your `convert()` function and print the result. Invalid arguments must return a helpful message.

### Live Currency Conversion

Instead of using fixed values in `currency.py`, you may retrieve real-time exchange rates using a public API such as:

```
https://api.exchangerate.host/convert?from=USD&to=EUR
```

Requirements for this:

* Use `urllib.request` or `http.client` (no external packages).
* Implement a fallback default rate (e.g., 1 USD = 0.9 EUR) in case of network failure or API errors.
* Your code must be testable even if offline.
* If you complete this, the test suite may check for accuracy within an acceptable range.

## Submission

1. **GitHub Repository**

   * Create a public repository named:

     ```
     unitflex-<your_name>
     ```

     Replace `<your_name>` with your actual name or GitHub username.

   * Push your full project to the repository, including:

     * All source code
     * `dist/` folder with the built package
     * `README.md`

   * Add the user `rassulya` as a **collaborator** to your GitHub repository to allow access.

2. Do not include `.venv`, `.mypy_cache`, or `__pycache__` directories in the repository.

## Rules

* Do not use any AI-generated code or code not understood by you.
* Your submission must run correctly in a clean environment.
* You may not modify the test suite or the provided folder structure.

