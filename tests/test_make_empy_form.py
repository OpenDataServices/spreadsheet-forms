import os

from spreadsheetforms.api import make_empty_form

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_DATA_OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "out"
)


def test_1():

    outfile = os.path.join(TEST_DATA_OUT_DIR, "test_1.xlsx")

    make_empty_form(os.path.join(TEST_DATA_DIR, "pet1.xlsx"), outfile)

    # TODO actually test output file - for now we just dump it in a known place so a human can have a look
