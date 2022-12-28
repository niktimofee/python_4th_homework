# 📍 Программа, которая формирует случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записывает в файл многочлен заданой натуральной степени k.

import random

k = int(input('✏️  Введите значение степени (k): '))

def create_multipliers_list(k):
    random_multipliers_list = [random.randint(0, 100) for i in range(k+1)]
    return random_multipliers_list

def create_polynomial(mp):
    temp_list = mp[::-1]
    eq = ''
    if len(temp_list) < 1:
        eq = 'x = 0'
    else:
        for i in range(len(temp_list)):
            if i != len(temp_list) - 1 and temp_list[i] != 0 and i != len(temp_list) - 2:
                eq += f'{temp_list[i]}x^{len(temp_list)-i-1}'
                if temp_list[i+1] != 0:
                    eq += ' + '
            elif i == len(temp_list) - 2 and temp_list[i] != 0:
                eq += f'{temp_list[i]}x'
                if temp_list[i+1] != 0:
                    eq += ' + '
            elif i == len(temp_list) - 1 and temp_list[i] != 0:
                eq += f'{temp_list[i]} = 0'
            elif i == len(temp_list) - 1 and temp_list[i] == 0:
                eq += ' = 0'
    return eq

def write_file(res):
    with open('4_file.txt', 'w') as data:
        data.write(res)

multipliers_list = create_multipliers_list(k)
write_file(create_polynomial(multipliers_list))
with open('4_file.txt', 'r') as data:
    poly_res = data.readlines()
print(f'📝 Результат {poly_res} записан в файл "4_file.txt"')