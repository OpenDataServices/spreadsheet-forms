import datetime
import os

import pytest

from spreadsheetforms.api import (
    GetDataFromFormMissingWorksheetAction,
    get_data_from_form,
    make_empty_form,
)
from spreadsheetforms.exceptions import MissingWorksheetException

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_DATA_OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "out"
)


def test_1():

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "pet1.xlsx"),
        os.path.join(TEST_DATA_DIR, "cat1.xlsx"),
    )

    assert {
        "noise": "Miaow Miaow Purr Purr Hiss",
        "pet": "Cat",
        "hungry": [
            {"state": "Yes", "wants": "Food"},
            {"state": "Always", "wants": "Food"},
            {"state": "Right Now", "wants": "Food"},
        ],
        "sleepy": [
            {"state": "A lot", "wants": "Sleep"},
            {"state": "Also Right Now", "wants": "A Nap"},
        ],
        "toys": [
            {"title": "Bit of string", "squeak": "No"},
            {"title": "Marble", "squeak": "No"},
        ],
    } == data


def test_missing_worksheet_errors_1():

    with pytest.raises(MissingWorksheetException):
        get_data_from_form(
            os.path.join(TEST_DATA_DIR, "pet1.xlsx"),
            os.path.join(TEST_DATA_DIR, "cat1-missingworksheet.xlsx"),
        )


def test_missing_worksheet_provides_no_data_1():

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "pet1.xlsx"),
        os.path.join(TEST_DATA_DIR, "cat1-missingworksheet.xlsx"),
        missing_worksheet_action=GetDataFromFormMissingWorksheetAction.SET_NO_DATA,
    )

    assert {
        "noise": "Miaow Miaow Purr Purr Hiss",
        "pet": "Cat",
        "hungry": [
            {"state": "Yes", "wants": "Food"},
            {"state": "Always", "wants": "Food"},
            {"state": "Right Now", "wants": "Food"},
        ],
        "sleepy": [
            {"state": "A lot", "wants": "Sleep"},
            {"state": "Also Right Now", "wants": "A Nap"},
        ],
    } == data


def test_deep():

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "pet1-deep.xlsx"),
        os.path.join(TEST_DATA_DIR, "cat1.xlsx"),
    )

    assert {
        "emits": {"noise": "Miaow Miaow Purr Purr Hiss"},
        "pet": {"kind": "Cat"},
        "mood": {
            "hungry": [
                {"current": {"state": "Yes", "wants": "Food"}},
                {"current": {"state": "Always", "wants": "Food"}},
                {"current": {"state": "Right Now", "wants": "Food"}},
            ],
            "sleepy": [
                {"current": {"state": "A lot", "wants": "Sleep"}},
                {"current": {"state": "Also Right Now", "wants": "A Nap"}},
            ],
        },
        "likes": {
            "toys": [
                {
                    "human-concerns": {"title": "Bit of string"},
                    "pet-concerns": {"squeak": "No"},
                },
                {
                    "human-concerns": {"title": "Marble"},
                    "pet-concerns": {"squeak": "No"},
                },
            ]
        },
    } == data


def test_formats_1():

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "formats1.xlsx"),
        os.path.join(TEST_DATA_DIR, "formats1-data1.xlsx"),
    )
    assert {
        "currency": "$1.23",
        "date": datetime.datetime(2020, 10, 27, 0, 0),
        "number": 1.456,
        "string": "CATS",
    } == data


def test_formats_1_date_format():

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "formats1.xlsx"),
        os.path.join(TEST_DATA_DIR, "formats1-data1.xlsx"),
        date_format="%Y-%m-%d",
    )
    assert {
        "currency": "$1.23",
        "date": "2020-10-27",
        "number": 1.456,
        "string": "CATS",
    } == data


def test_empty_form_loads_none():
    # This is default behaviour, but we probably want to have more options
    # around this soon so putting in a test to work aganist later

    outfile = os.path.join(TEST_DATA_OUT_DIR, "test_empty.xlsx")

    make_empty_form(os.path.join(TEST_DATA_DIR, "pet1.xlsx"), outfile)

    data = get_data_from_form(
        os.path.join(TEST_DATA_DIR, "pet1.xlsx"),
        outfile,
    )

    assert None == data["pet"]
