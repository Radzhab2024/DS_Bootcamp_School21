#!/usr/bin/env python3
import sys
import os
import psutil
import time


def read_file_with_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for read_line in file:
            yield read_line


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ./ordinary.py <path_to_file>')
        sys.exit(1)

    path_to_file = sys.argv[1]

    start_time = time.time()

    lines_gen = read_file_with_generator(path_to_file)

    for line in lines_gen:
        pass

    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 / 1024 / 1024

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Peak Memory Usage = {memory_usage:.3f} GB")
    print(f"User Mode Time + System Mode Time = {elapsed_time:.2f}s")
