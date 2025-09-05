#!/usr/bin/env python3
import os


def in_virtenv():
    env_name = os.environ.get('VIRTUAL_ENV')
    if env_name:
        print(f'Your current environment is {env_name}')
    else:
        print('No active environment')


if __name__ == '__main__':
    in_virtenv()
