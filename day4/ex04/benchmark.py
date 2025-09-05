#!/usr/bin/env python3

import timeit
import random
from collections import Counter


def create_random_list():
    """Создает список из 1000000 случайных чисел от 0 до 100"""
    return [random.randint(0, 100) for _ in range(1000000)]


def count_with_dict(random_numbers_list):
    """Считает количество значений с помощью словаря"""
    counts_dict = {}
    for number in random_numbers_list:
        if number in counts_dict:
            counts_dict[number] += 1
        else:
            counts_dict[number] = 1
    return counts_dict


def top_10_with_dict(random_numbers_list):
    """Получает 10 самых часто встречающихся числа из словаря"""
    counts_dict = count_with_dict(random_numbers_list)
    sorted_counts = sorted(counts_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


def count_with_counter(random_numbers_list):
    return Counter(random_numbers_list)


def top_10_by_counter(random_numbers_list):
    counter = Counter(random_numbers_list)
    return counter.most_common(10)


def benchmark_work():
    numbers = create_random_list()
    dict_time = timeit.timeit(lambda: count_with_dict(numbers), number=10)
    counter_time = timeit.timeit(lambda: count_with_counter(numbers), number=10)
    print(f'my function: {dict_time}')
    print(f'Counter: {counter_time}')
    dict_top_10 = timeit.timeit(lambda: top_10_by_counter(numbers), number=10)
    counter_top_10 = timeit.timeit(lambda: top_10_by_counter(numbers), number=10)
    print(f'my top: {dict_top_10}')
    print(f"Counter's top: {counter_top_10}")


if __name__ == '__main__':
    benchmark_work()
