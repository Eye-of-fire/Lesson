def calculate_structure_sum(data):
    sum_ = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, dict):
        data = list(data.items())
    for dict_values in data:
        sum_ += calculate_structure_sum(dict_values)
    return sum_

data_structure = [[1, 2, 3], {'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),
"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)