from jsonpointer import JsonPointerException, resolve_pointer


def json_set_deep_value(data, key, value):
    key_bits = key.split("/")

    # Have to navigate to right bit of structure, creating dicts as we go
    if len(key_bits) > 1:
        for idx in range(0, len(key_bits) - 1):

            key_bit = key_bits[idx]
            if key_bit not in data:
                data[key_bit] = {}

            data = data[key_bit]

    # Finally, set value
    data[key_bits[-1]] = value


def json_append_deep_value(data, key, value):
    key_bits = key.split("/")

    # Have to navigate to right bit of structure, creating dicts as we go
    if len(key_bits) > 1:
        for idx in range(0, len(key_bits) - 1):

            key_bit = key_bits[idx]
            if key_bit not in data:
                data[key_bit] = {}

            data = data[key_bit]

    # Finally, append value
    data[key_bits[-1]].append(value)


def json_get_deep_value(data, key):
    try:
        return resolve_pointer(data, "/" + key)
    except JsonPointerException:
        return None
