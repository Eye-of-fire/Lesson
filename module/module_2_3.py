my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    list_ = my_list[a]
    a += 1
    if list_ == 0:
        continue
    elif list_ < 0:
        break
    else:
        print(list_)