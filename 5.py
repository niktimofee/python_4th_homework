# 📍 Программа, которая формирует файл, содержащий сумму многочленов находящихся в других двух разных файлах.

import random

def create_polynomial(mp):
    temp_list = mp[::-1]
    eq = ''
    if len(temp_list) < 1:
        eq = 'x = 0'
    else:
        for i in range(len(temp_list)):
            if i != len(temp_list) - 1 and temp_list[i] != 0 and i != len(temp_list) - 2:
                eq += f'{temp_list[i]}x^{len(temp_list)-i-1}'
                if temp_list[i+1] != 0 or temp_list[i+2] != 0:
                    eq += ' + '
            elif i == len(temp_list) - 2 and temp_list[i] != 0:
                eq += f'{temp_list[i]}x'
                if temp_list[i+1] != 0 or temp_list[i+2] != 0:
                    eq += ' + '
            elif i == len(temp_list) - 1 and temp_list[i] != 0:
                eq += f'{temp_list[i]} = 0'
            elif i == len(temp_list) - 1 and temp_list[i] == 0:
                eq += ' = 0'
    return eq

def poly_deg(l):
    if 'x^' in l:
        i = l.find('^')
        num = int(l[i+1:])
    elif ('x' in l) and ('^' not in l):
        num = 1
    else:
        num = -1
    return num

def poly_term_mp(l):
    if 'x' in l:
        i = l.find('x')
        num = int(l[:i])
    return num

def poly_calc(p):
    p = p[0].replace(' ', '').split('=')
    p = p[0].split('+')
    temp_list = []
    l = len(p)
    if poly_deg(p[-1]) == -1:
        temp_list.append(int(p[-1]))
        l -= 1
    dg = 1
    i = l-1
    while i >= 0:
        if poly_deg(p[i]) != -1 and poly_deg(p[i]) == dg:
            temp_list.append(poly_term_mp(p[i]))
            i -= 1
            dg += 1
        else:
            temp_list.append(0)
            dg += 1

    return temp_list

def write_file(res):
    with open('5_result.txt', 'w') as data:
        data.write(res)

with open('5_poly1.txt', 'r') as data:
    poly1 = data.readlines()

with open('5_poly2.txt', 'r') as data:
    poly2 = data.readlines()

print(f'Первый многочлен из файла "5_poly1.txt" : {poly1}')
print(f'Второй многочлен из файла "5_poly2.txt" : {poly2}')

poly1_temp = poly_calc(poly1)
poly2_temp = poly_calc(poly2)
ll = len(poly1_temp)
if len(poly1_temp) > len(poly2_temp):
    ll = len(poly2_temp)
poly_sum = [poly1_temp[i] + poly2_temp[i] for i in range(ll)]
if len(poly1_temp) > len(poly2_temp):
    mm = len(poly1_temp)
    for i in range(ll, mm):
        poly_sum.append(poly1_temp[i])
else:
    mm = len(poly2_temp)
    for i in range(ll, mm):
        poly_sum.append(poly2_temp[i])

write_file(create_polynomial(poly_sum))
with open('5_result.txt', 'r') as data:
    poly_res = data.readlines()
print(f'📝 Результат сложения двух многочленов {poly_res} записан в файл "5_result.txt"')