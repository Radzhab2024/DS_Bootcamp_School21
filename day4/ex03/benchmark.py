#!/usr/bin/env python3

import timeit
import sys
from functools import reduce


def get_function_name():
    """Получает имя функции из аргументов командной строки"""
    if len(sys.argv) != 4:
        print('Usage: .ordinary.py <function_name> <number_of_calls> <number_of_numbers>')
        sys.exit(1)

    function_name = sys.argv[1]
    valid_functions = ['loop', 'reduce']
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


def get_number_of_numbers():
    """Получает количество чисел из командной строки"""
    try:
        number_of_numbers = int(sys.argv[3])
        if number_of_numbers <= 0:
            raise ValueError('Number of calls must be positive')
        return number_of_numbers
    except ValueError:
        print('Number of calls must be integer')
        sys.exit(1)


def get_sum_by_loop(numbers):
    total_sum = 0
    for number in range(1, numbers + 1):
        total_sum += number * number
    return total_sum


def get_sum_by_reduce(numbers):
    return reduce(lambda total_sum, number: total_sum + number * number, range(1, numbers + 1))


def benchmark_work(function_name, number_of_calls, number_of_numbers):
    loop_time = timeit.timeit(lambda: get_sum_by_loop(number_of_numbers), number=number_of_calls)
    reduce_time = timeit.timeit(lambda: get_sum_by_reduce(number_of_numbers), number=number_of_calls)
    results = {
        'loop': loop_time,
        'reduce': reduce_time
    }
    print(results[function_name])


if __name__ == '__main__':
    entered_function_name = get_function_name()
    entered_number_of_calls = get_number_of_calls()
    entered_number_of_numbers = get_number_of_numbers()
    benchmark_work(entered_function_name, entered_number_of_calls, entered_number_of_numbers)
