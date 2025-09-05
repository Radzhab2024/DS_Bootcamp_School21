#!/usr/bin/env python3

import timeit
import sys


def get_function_name():
    """Получает имя функции из аргументов командной строки"""
    if len(sys.argv) != 3:
        print('Usage: .ordinary.py <function_name> <number_of_calls>')
        sys.exit(1)

    function_name = sys.argv[1]
    valid_functions = ['loop', 'list comprehension', 'map', 'filter']
    if function_name not in valid_functions:
        print(f'Invalid function name. Valid names are: {valid_functions}')
        sys.exit(1)
    return function_name


def get_number_of_calls():
    """Получает количество вызовов из аргументов командной строки."""
    try:
        number_of_calls = int(sys.argv[2])
        if number_of_calls <= 0:
            raise ValueError('Number of calls must be positive')
        return number_of_calls
    except ValueError:
        print('Number of calls must be integer')
        sys.exit(1)


def create_emails_list():
    """Создает список электронных адресов"""
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5


def get_gmails_by_loop(emails_list):
    """Фильтрует e-mail адреса с помощью цикла"""
    gmails = []
    for email in emails_list:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


def get_gmails_by_list_comprehension(emails_list):
    """Фильтрует e-mail адреса с спсикового включения"""
    gmails = [email for email in emails_list if email.endswith('@gmail.com')]
    return gmails


def get_gmails_by_map(emails_list):
    """Фильтрует e-mail адреса с помощью функции map"""
    return list(map(lambda email: email if email.endswith('@gmail.com') else None, emails_list))


def get_gmails_by_filter(emails_list):
    return filter(lambda email: email.endswith('@gmail.com'), emails_list)


def benchmark_work(function_name, number_of_calls):
    adresses_list = create_emails_list()
    loop_time = timeit.timeit(lambda: get_gmails_by_loop(adresses_list), number=number_of_calls)
    comprehension_time = timeit.timeit(lambda: get_gmails_by_list_comprehension(adresses_list), number=number_of_calls)
    map_time = timeit.timeit(lambda: get_gmails_by_map(adresses_list), number=number_of_calls)
    filter_time = timeit.timeit(lambda: get_gmails_by_filter(adresses_list), number=number_of_calls)

    results = {
        'loop': loop_time,
        'list comprehension': comprehension_time,
        'map': map_time,
        'filter': filter_time
    }

    print(results[function_name])


if __name__ == '__main__':
    entered_function_name = get_function_name()
    entered_number_of_calls = get_number_of_calls()
    benchmark_work(entered_function_name, entered_number_of_calls)
