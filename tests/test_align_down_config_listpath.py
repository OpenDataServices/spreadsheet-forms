import os
import pytest
from spreadsheetforms.api import get_data_from_form

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def test_down_confing_same_column():
    """Test that the down config works when the listpath is in the same column."""

    guide_filename = os.path.join(TEST_DATA_DIR, "pet1-deep-down.xlsx")
    input_filename = os.path.join(TEST_DATA_DIR, "cat1.xlsx")

    # Run the current function with the input files
    data = get_data_from_form(guide_filename, input_filename)

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
    } == data, "Data mismatch detected!"
