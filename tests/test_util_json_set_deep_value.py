from spreadsheetforms.util import json_set_deep_value


def test_1():
    data = {}
    json_set_deep_value(data, "cat", "cool")
    assert data == {"cat": "cool"}


def test_2():
    data = {}
    json_set_deep_value(data, "cat/name", "Bob")
    assert data == {"cat": {"name": "Bob"}}


def test_3():
    data = {}
    json_set_deep_value(data, "cat/name/official", "Mr Bob The Magnificent")
    json_set_deep_value(data, "cat/name/informal", "Bob")
    assert data == {
        "cat": {"name": {"informal": "Bob", "official": "Mr Bob The Magnificent"}}
    }
