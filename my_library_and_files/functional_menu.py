from my_library_and_files. library import functional_task as ft
from my_library_and_files import start_menu as sm
from my_library_and_files import print_text as pt

def functional():
    functionStart = input('\033[33mВыберите задачу: \033[0m')
    
    if functionStart == 'menu' or functionStart == 'stop':
        match functionStart:
            case 'menu': # Выход в главное меню
                sm.main_menu()
            case 'stop': # Завершение работы
                print(pt.completion_of_work())
                exit()
    elif functionStart != 'menu' or functionStart != 'stop':
        functionStart = int(functionStart)
        if 0 <= functionStart < 7: 
            match functionStart:
                case 0: # Вывод списка задач
                    print(pt.list_of_tasks())
                    functional()
                case 1: # Треугольник
                    print(pt.triangle_text())
                    ft.triangle()
                    functional()
                case 2: # Простые или составные числа
                    print(pt.simple_or_complex_text())
                    ft.simple_or_complex()
                    functional()
                case 3: # Високосный ли год?
                    print(pt.leap_year_text())
                    ft.leap_year()
                    functional()
                case 4: # Что за число введено?
                    print(pt.what_is_the_number_entered_text())
                    ft.what_is_the_number_entered()
                    functional()
                case 5: # Ёлочка из звёздочек!
                    print(pt.tree_star_text1())
                    ft.tree_star()
                    functional()
                case 6: # Таблица умножения
                    print(pt.multiplication_table_text())
                    ft.multiplication_table()
                    functional()
        else:
            print(pt.error_input())
            functional()

    else:
        print(pt.error_input())
        functional()