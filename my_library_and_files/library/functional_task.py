from my_library_and_files import print_text as pt
from my_library_and_files import functional_menu as mfm

# Треугольник
def triangle():
    a = int(input('\033[33mВведите первую сторону треугольника: \033[0m'))
    b = int(input('\033[33mВведите вторую сторону треугольника: \033[0m'))
    c = int(input('\033[33mВведите третью сторону треугольника: \033[0m'))

    sumAB = a + b
    sumAC = a + c
    sumBC = b + c

    if a <= sumBC and b <= sumAC and c <= sumAB:
        print('\033[32mТреугольник существует!\033[0m')
        if a == b == c == a:
            print('\033[32mтреугольник равносторонний!\033[0m')
        elif a != b != c != a:
            print('\033[32mтреугольник разносторонний!\033[0m')
        elif a == b != c or b == c != a or a == c != b:
            print('\033[32mтреугольник равнобедренный!\033[0m')
    else:
        print('\033[32mТреугольник не существует!\033[0m')

# Простые или составные числа
def simple_or_complex():
    i = 2
    counter = 0
    NOT_SIMPLE = 1
    MIN = 0
    MAX = 100000
    number = int(input('\033[33mВведите число в диапазоне от 0 до 100000: \033[0m'))

    if number == 0:
        print('\033[32mВы ввели 0 и вернётесь в меню!\033[0m')
        mfm.functional()
    else:
        while True:
            if MIN < number < MAX:
                while i <= number - 1:
                    if number % i == 0:
                        counter += 1
                    i += 1
                if counter >= NOT_SIMPLE:
                    print('\033[32mЧисло составное!\033[0m')
                    simple_or_complex()
                else:
                    print('\033[32mЧисло простое!\033[0m')
                    simple_or_complex()
                break
            else:
                print('\033[31mНедопустимое значение!\033[0m')
                simple_or_complex()


# Високосный ли год?
def leap_year():
    year = int(input('\033[33mВведите год для проверки его на високосность: \033[0m'))
    if year == 0000:
        print('\033[32mВы ввели 0000 и вернётесь в меню!\033[0m')
        mfm.functional()
    else:
        if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
            print('\033[32mГод високосный!\033[0m')
            leap_year()
        else:
            print('\033[32mГод не високосный!\033[0m')
            leap_year()

# Что за число введено?
def what_is_the_number_entered():
    number = int(input('\033[33mВведите число от 1 до 999: \033[0m'))
    if number == 0:
        print('\n\033[32mВы ввели 0 и вернётесь в меню!\033[0m\n')
        mfm.functional()
    else:
        if 0 < number < 1000:
            if 0 < number < 10:
                print('\n\033[32mВы ввели однозначное число!\033[0m')
                kvnum = number ** 2
                print(f'\033[32mКвадрат введённой цифры {number} равен {kvnum}!\033[0m\n')
                what_is_the_number_entered()
            elif 10 <= number < 100:
                print('\n\033[32mВы ввели двузначное число!\033[0m')
                num1 = (number % 100) // 10
                num2 = number % 10
                rezult = num1 * num2
                print(f'\033[32mПроизведение цифр числа {number} равно {rezult}!\033[0m\n')
                what_is_the_number_entered()
            elif 100 <= number < 1000:
                print('\n\033[32mВы ввели трёхзначное число!\033[0m')
                numberKop = number
                n2 = 0
                while number > 0:
                    digit = number % 10
                    number = number // 10
                    n2 = n2 * 10
                    n2 = n2 + digit
                print(f'\033[32mДля трёхзначного числа {numberKop} его зеркальное отображение равно {n2}!\033[0m\n')
                what_is_the_number_entered()
        else:
            print('\n\033[31mВы ввели неправильное число, повторите попытку!\033[0m\n')
            what_is_the_number_entered()


# Ёлочка из звёздочек!
def tree_star():
    p = int(input('\033[33mУкажите число рядов ёлочки из звёздочек: \033[0m'))
    if p == 0:
        print('\033[32mВы ввели 0 и вернётесь в меню!\033[0m')
        mfm.functional()
    else:
        for i in range(p):
            print(' ' * (p - i), '*' * (2 * i + 1))
        print('')
        tree_star()

# Таблица умножения
def multiplication_table():
    for i1 in range(1, 11):
        for k1 in range(2, 6):
            print(f'{k1} * {i1} = {i1 * k1}\t', end='')
        print('')
    print()
    for i2 in range(1, 11):
        for k2 in range(6, 10):
            print(f'{k2} * {i2} = {i2 * k2}\t', end='')
        print('')
    print()