import os

import openpyxl

from spreadsheetforms.api import put_data_in_form

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_DATA_OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "out"
)


def test_1():

    outfile = os.path.join(TEST_DATA_OUT_DIR, "put_data_in_form_1.xlsx")

    data = {
        "noise": "Woof Woof",
        "pet": "Dog",
        "toys": [
            {"title": "Plastic bone", "squeak": "Oh Yes"},
            {"title": "Tennis Ball", "squeak": "No"},
        ],
    }

    put_data_in_form(os.path.join(TEST_DATA_DIR, "pet1.xlsx"), data, outfile)

    workbook = openpyxl.load_workbook(outfile, read_only=True)

    assert "Dog" == workbook["Info"]["B5"].value
    assert "Woof Woof" == workbook["Info"]["B6"].value
    assert "Plastic bone" == workbook["Toys"]["A7"].value
    assert "Oh Yes" == workbook["Toys"]["B7"].value
    assert "Tennis Ball" == workbook["Toys"]["A8"].value
    assert "No" == workbook["Toys"]["B8"].value


def test_deep():

    outfile = os.path.join(TEST_DATA_OUT_DIR, "put_data_in_form_1_deep.xlsx")

    data = {
        "emits": {"noise": "Woof Woof"},
        "pet": {"kind": "Dog"},
        "likes": {
            "toys": [
                {
                    "human-concerns": {"title": "Plastic bone"},
                    "pet-concerns": {"squeak": "Oh Yes"},
                },
                {
                    "human-concerns": {"title": "Tennis Ball"},
                    "pet-concerns": {"squeak": "No"},
                },
            ]
        },
    }

    put_data_in_form(os.path.join(TEST_DATA_DIR, "pet1-deep.xlsx"), data, outfile)

    workbook = openpyxl.load_workbook(outfile, read_only=True)

    assert "Dog" == workbook["Info"]["B5"].value
    assert "Woof Woof" == workbook["Info"]["B6"].value
    assert "Plastic bone" == workbook["Toys"]["A7"].value
    assert "Oh Yes" == workbook["Toys"]["B7"].value
    assert "Tennis Ball" == workbook["Toys"]["A8"].value
    assert "No" == workbook["Toys"]["B8"].value
