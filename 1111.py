# #random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# print(sales.items())


# # random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# items = sales.items()
# print('Original items:', items) # delete an item from dictionary
# del[sales['apple']]
# print('Updated items:', items)\


# def calculate_structure_sum(obj):
#     total = 0
#     if isinstance(obj, int):
#         return obj
#     elif isinstance(obj, str):
#         return len(obj)
#     elif isinstance(obj, dict):
#         obj = list(obj.items())
#     for value in obj:
#         total += calculate_structure_sum(value)
#     return total




# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])]
#
# result = calculate_structure_sum(data_structure)
# print(result)


# data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])
# # s = 0
# # for x in data:
# #     if isinstance(x, float):
# #         s += x
# s = sum(filter(lambda x: isinstance(x, float), data))
# print(s)

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