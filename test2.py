from pprint import pprint


def validate_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return value


def compare_files(first_file, second_file):
    compared_data = {}
    for el2 in second_file.keys():
        new_el = {}
        if isinstance(second_file[el2], dict) and \
        el2 in first_file.keys() and \
        second_file[el2] != first_file[el2]:
            new_el['status'] = 'nested'
            new_el['new_value'] = compare_files(
                first_file[el2], second_file[el2]
                )
            compared_data[el2] = new_el
        if el2 not in first_file.keys():
            new_el['status'] = 'added'
            new_el['new_value'] = second_file[el2]
            compared_data[el2] = new_el
        if el2 in first_file.keys() and\
        second_file[el2] == first_file[el2]:
            new_el['status'] = 'unchanged'
            new_el['old_value'] = first_file[el2]
            new_el['new_value'] = second_file[el2]
            compared_data[el2] = new_el
        if not isinstance(second_file[el2], dict) and \
        el2 in first_file.keys() and \
        second_file[el2] != first_file[el2]:
            new_el['status'] = 'changed'
            new_el['old_value'] = first_file[el2]
            new_el['new_value'] = second_file[el2]
            compared_data[el2] = new_el

    for el1 in first_file.keys():
        new_el = {}
        if el1 not in second_file.keys():
            new_el['status'] = 'removed'
            new_el['old_value'] = first_file[el1]
            compared_data[el1] = new_el

    return compared_data


first_file_data = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

second_file_data = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}




if __name__ == '__main__':
    pprint(compare_files(first_file_data, second_file_data))
