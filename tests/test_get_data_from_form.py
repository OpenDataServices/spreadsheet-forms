import datetime
import os

from spreadsheetforms.api import get_data_from_form

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
