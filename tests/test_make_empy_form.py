import os

import openpyxl

from spreadsheetforms.api import make_empty_form

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_DATA_OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "out"
)


def test_1():

    outfile = os.path.join(TEST_DATA_OUT_DIR, "test_1.xlsx")

    make_empty_form(os.path.join(TEST_DATA_DIR, "pet1.xlsx"), outfile)

    workbook = openpyxl.load_workbook(outfile, read_only=True)

    assert "Pet" == workbook["Info"]["A5"].value
    assert None == workbook["Info"]["B9"].value
    assert None == workbook["Info"]["B5"].value
    assert None == workbook["Info"]["B13"].value
    assert None == workbook["Info"]["B14"].value
    assert None == workbook["Toys"]["A7"].value
    assert None == workbook["Toys"]["B7"].value
