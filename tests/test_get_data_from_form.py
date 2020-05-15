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
