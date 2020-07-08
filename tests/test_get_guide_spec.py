import os

from spreadsheetforms.api import get_guide_spec

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_1():

    guide_spec = get_guide_spec(os.path.join(TEST_DATA_DIR, "pet1.xlsx"))

    assert {
        "worksheets": {
            "Info": {
                "single_configs": {
                    "pet": {
                        "mode": "single",
                        "path": "pet",
                        "coordinate": "B5",
                        "column_letter": "B",
                        "column": 2,
                        "row": 5,
                    },
                    "noise": {
                        "mode": "single",
                        "path": "noise",
                        "coordinate": "B6",
                        "column_letter": "B",
                        "column": 2,
                        "row": 6,
                    },
                },
                "down_configs": {},
                "right_configs": {
                    "hungry": [
                        {
                            "mode": "right",
                            "list_path": "hungry",
                            "item_path": "state",
                            "coordinate": "B9",
                            "column_letter": "B",
                            "column": 2,
                            "row": 9,
                        },
                        {
                            "mode": "right",
                            "list_path": "hungry",
                            "item_path": "wants",
                            "coordinate": "B10",
                            "column_letter": "B",
                            "column": 2,
                            "row": 10,
                        },
                    ],
                    "sleepy": [
                        {
                            "mode": "right",
                            "list_path": "sleepy",
                            "item_path": "state",
                            "coordinate": "B13",
                            "column_letter": "B",
                            "column": 2,
                            "row": 13,
                        },
                        {
                            "mode": "right",
                            "list_path": "sleepy",
                            "item_path": "wants",
                            "coordinate": "B14",
                            "column_letter": "B",
                            "column": 2,
                            "row": 14,
                        },
                    ],
                },
            },
            "Toys": {
                "single_configs": {},
                "down_configs": {
                    "toys": [
                        {
                            "mode": "down",
                            "list_path": "toys",
                            "item_path": "title",
                            "coordinate": "A7",
                            "column_letter": "A",
                            "column": 1,
                            "row": 7,
                        },
                        {
                            "mode": "down",
                            "list_path": "toys",
                            "item_path": "squeak",
                            "coordinate": "B7",
                            "column_letter": "B",
                            "column": 2,
                            "row": 7,
                        },
                    ]
                },
                "right_configs": {},
            },
        }
    } == guide_spec
