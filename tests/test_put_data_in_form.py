import os

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

    # TODO actually test output file - for now we just dump it in a known place so a human can have a look
