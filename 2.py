# 📍 Программа, которая составляет список простых множителей натурального числа N.

num = int(input('✏️  Введите число N: '))
i = 2  # первое простое число
my_list = []
inp_num = num
while i <= num:
    if num % i == 0:
        my_list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'Список простых множителей числа {inp_num} => {my_list}')