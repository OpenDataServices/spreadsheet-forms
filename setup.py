from setuptools import setup

install_requires = ["openpyxl>=3.0", "jsonpointer"]

setup(
    name="spreadsheetforms",
    version="0.4.0",
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    packages=["spreadsheetforms"],
    scripts=[],
    url="https://github.com/OpenDataServices/spreadsheet-forms",
    license="MIT",
    description="Tools for forms in spreadsheets; creating, extracting submitted data and filling with data",
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={"dev": ["pytest", "flake8", "isort", "black"]},
)
