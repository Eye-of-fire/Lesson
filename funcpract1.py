def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_
print(find_max([1,6,3,4,5]))


def count_even(list_2):
    counter = 0
    for i in list_2:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter
print(count_even([1,2,3,0,4,5,6]))

def unique(list_3):
    new_list = []
    for i in list_3:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique([1,2,3,0,4,5,6,1,2,3,0,4,5,6]))