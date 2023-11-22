import os
import pytest

from spreadsheetforms.api import get_data_from_form
from spreadsheetforms.exceptions import MisalignedDownConfigException

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_misaligned_down_configs_exception():
    guide_filename = os.path.join(TEST_DATA_DIR, "pet1-deep-down.xlsx")
    input_filename = os.path.join(TEST_DATA_DIR, "cat1.xlsx")

    # Expect MisalignedDownConfigException to be raised when processing the misconfigured sheet
    with pytest.raises(MisalignedDownConfigException):
        get_data_from_form(guide_filename, input_filename)
