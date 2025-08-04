from pprint import pprint
from test2 import compare_files


def validate_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return value


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

compared_files = compare_files(first_file_data, second_file_data)
# pprint(compared_files)


def create_dict(dictionary):
    result_string = '{\n'
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result_string += f'    {key}: {create_dict(value)}\n'
        else:
            result_string += f'    {key}: {value}\n'
    result_string += '}'
    return result_string


def create_string(compared_data):
    result_report = '{\n'
    for el in sorted(compared_data.keys()):
        # print({el: compared_data[el]})
        if compared_data[el]['status'] == 'nested':
            result_report += \
            f'{el}: {create_string(compared_data[el]['new_value'])}\n'
        if compared_data[el]['status'] == 'removed':
            if isinstance(compared_data[el]['old_value'], dict):
                result_report += \
                f'  - {el}: {create_dict(compared_data[el]['old_value'])}\n'
            else:
                result_report += \
                f'  - {el}: {validate_value(compared_data[el]['old_value'])}\n'
        if compared_data[el]['status'] == 'unchanged':
            if isinstance(compared_data[el]['new_value'], dict):
                result_report += \
                f'    {el}: {create_dict(compared_data[el]['new_value'])}\n'
            else:
                result_report += \
                f'    {el}: {validate_value(compared_data[el]['new_value'])}\n'
        if compared_data[el]['status'] == 'changed':
            if isinstance(compared_data[el]['old_value'], dict):
                result_report += \
                f'  - {el}: {create_dict(compared_data[el]['old_value'])}\n'
            else:
                result_report += \
                f'  - {el}: {validate_value(compared_data[el]['old_value'])}\n'
            if isinstance(compared_data[el]['new_value'], dict):
                result_report += \
                f'  + {el}: {create_dict(compared_data[el]['new_value'])}\n'
            else:
                result_report += \
                f'  + {el}: {validate_value(compared_data[el]['new_value'])}\n'
        if compared_data[el]['status'] == 'added':
            if isinstance(compared_data[el]['new_value'], dict):
                result_report += \
                f'  + {el}: {create_dict(compared_data[el]['new_value'])}\n'
            else:
                result_report += \
                f'  + {el}: {validate_value(compared_data[el]['new_value'])}\n'
    result_report += '}'
    return result_report


print(create_string(compared_files))
