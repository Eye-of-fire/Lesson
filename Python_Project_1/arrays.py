import timeit
from module_4.sortfunc import insertion_sort,bubble_sort, selection_sort

data_1 = [9,8,5,3,4,1,2]
data_2 = [9,8,5,3,4,1,2,7,0]
data_3 = [9,8,5,3,4,1,2,7,0,6,10]
print('__________________________________insertion_sort(data_1)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('insertion_sort(data_1)', globals=globals()),2),'сек')
print(insertion_sort(data_1))
print('__________________________________insertion_sort(data_2)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('insertion_sort(data_2)', globals=globals()),2),'сек')
print(insertion_sort(data_2))
print('__________________________________insertion_sort(data_3)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('insertion_sort(data_2)', globals=globals()),2),'сек')
print(insertion_sort(data_3))

print('__________________________________bubble_sort(data_1)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('bubble_sort(data_1)', globals=globals()),2),'сек')
print(bubble_sort(data_1))
print('__________________________________bubble_sort(data_2)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('bubble_sort(data_2)', globals=globals()),2),'сек')
print(bubble_sort(data_2))
print('__________________________________bubble_sort(data_3)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('bubble_sort(data_2)', globals=globals()),2),'сек')
print(bubble_sort(data_3))

print('__________________________________selection_sort(data_1)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('selection_sort(data_1)', globals=globals()),2),'сек')
print(selection_sort(data_1))
print('__________________________________selection_sort(data_2)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('selection_sort(data_2)', globals=globals()),2),'сек')
print(selection_sort(data_2))
print('__________________________________selection_sort(data_3)___________________________________________________')
print('Время вычисление =',round(timeit.timeit('selection_sort(data_2)', globals=globals()),2),'сек')
print(selection_sort(data_3))

