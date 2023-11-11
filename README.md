# Spreadsheet Forms

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/OpenDataServices/spreadsheet-forms)

Spreadsheet Forms is a Python library that simplifies the process of working with data from forms in spreadsheets by converting them to and from JSON format.

With Spreadsheet Forms, you can:

- Generate blank spreadsheet templates for consistent data collection.
- Easily pre-fill spreadsheets with existing data for verification or updates.
- Convert structured spreadsheet data into JSON for convenient storage or processing.

A customisable guide form spreadsheet dictates the data's structure, ensuring precision and order in your workflow.

For more details on package distribution, visit [Spreadsheet Forms on PyPI](https://pypi.org/project/spreadsheetforms/).

## Getting Started

Ensure you have Python 3.7 or higher installed and then install Spreadsheet Forms using pip:

```bash
pip install spreadsheetforms
```

## Example Usage

The following example demonstrates how to use the [get_data_from_form](https://spreadsheet-forms.readthedocs.io/en/latest/api/get_data_from_form.html) function to extract data from a spreadsheet form:

```python
from spreadsheetforms.api import get_data_from_form, GetDataFromFormMissingWorksheetAction

data = get_data_from_form(
    guide_filename,
    in_filename,
    date_format=None,
    missing_worksheet_action=GetDataFromFormMissingWorksheetAction.RAISE_EXCEPTION
)
```

For detailed information on all available functions and their usage, please refer to our [comprehensive documentation](https://spreadsheet-forms.readthedocs.io/en/latest/).

## Developer Setup

To contribute to Spreadsheet Forms, start by cloning the repository and setting up a development environment:

### Quick Start

Clone the latest version of the repository:

```bash
git clone https://github.com/OpenDataServices/spreadsheet-forms.git
cd spreadsheet-forms
```

Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the package in editable mode with the development dependencies:

```bash
pip install '.[dev]'
```

### Testing

We use [pytest](https://docs.pytest.org/en/latest/) for testing.

To run the test suite in verbose mode:

```bash
pytest -v
```

### Docker

We use [Docker](https://www.docker.com/) to run LibreOffice in a container to review document outputs.

To build the LibreOffice container:

```bash
docker-compose up
```

### Documentation Editing

We use [Sphinx](https://www.sphinx-doc.org/en/master/) for documentation.

To build the documentation locally:

```bash
sphinx-build -M html ./docs ./docs/_build/html
open docs/_build/html/index.html
```

To hot reload the documentation locally:

```bash
sphinx-autobuild ./docs ./docs/_build/html
```

## Contributing

We welcome and encourage public contributions to Spreadsheet Forms!

Please read our [Developer Docs](https://opendataservices.gitbook.io/developer-docs/) for more information about how we get our work done at [Open Data Services](https://opendataservices.coop/).

You can also reach out to us on our [GitHub account](https://github.com/opendataservices).

## License

This project is licensed under the [MIT License](LICENSE).
