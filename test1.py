def validate_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


compared_data = []
first_file_data = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
second_file_data = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}
for el2 in second_file_data.keys():
    new_el = {}
    if el2 not in first_file_data.keys():
        new_el['status'] = 'added'
        new_el['new_value'] = second_file_data[el2]
        compared_data.append({el2: new_el})
    if el2 in first_file_data.keys() and\
    second_file_data[el2] == first_file_data[el2]:
        new_el['status'] = 'unchanged'
        new_el['old_value'] = first_file_data[el2]
        new_el['new_value'] = second_file_data[el2]
        compared_data.append({el2: new_el})
    if el2 in first_file_data.keys() and\
    second_file_data[el2] != first_file_data[el2]:
        new_el['status'] = 'changed'
        new_el['old_value'] = first_file_data[el2]
        new_el['new_value'] = second_file_data[el2]
        compared_data.append({el2: new_el})
for el1 in first_file_data.keys():
    new_el = {}
    if el1 not in second_file_data.keys():
        new_el['status'] = 'removed'
        new_el['old_value'] = first_file_data[el1]
        compared_data.append({el1: new_el})
compared_data = sorted(compared_data,\
                        key=lambda x: sorted(x.keys())[0] if x else '')
result_report = '{\n'
for el in compared_data:
    for sideEl in el:
        if el[sideEl]['status'] == 'removed':
            result_report += \
              f'  - {sideEl}: {validate_value(el[sideEl]['old_value'])}\n'
        if el[sideEl]['status'] == 'unchanged':
            result_report += \
              f'    {sideEl}: {validate_value(el[sideEl]['new_value'])}\n'
        if el[sideEl]['status'] == 'changed':
            result_report += \
              f'  - {sideEl}: {validate_value(el[sideEl]['old_value'])}\n'
            result_report += \
              f'  + {sideEl}: {validate_value(el[sideEl]['new_value'])}\n'
        if el[sideEl]['status'] == 'added':
            result_report += \
              f'  + {sideEl}: {validate_value(el[sideEl]['new_value'])}\n'
result_report += '}'
print(compared_data)
print(result_report)
