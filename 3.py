# 📍 Программа, которая выводит список неповторяющихся элементов исходной последовательности чисел.

inp_list = list(map(int, input('✏️  Введите числа через пробел:\n').split( )))
new_list = []
[new_list.append(i) for i in inp_list if i not in new_list]
print(f'📜 Список неповторяющихся элементов => {new_list}')