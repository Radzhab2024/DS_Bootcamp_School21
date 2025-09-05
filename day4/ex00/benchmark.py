import timeit


def create_emails_list():
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5


def get_gmails_by_loop(emails_list):
    gmails = []
    for email in emails_list:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


def get_gmails_by_list_comprehension(emails_list):
    gmails = [email for email in emails_list if email.endswith('@gmail.com')]
    return gmails


def benchmark_work():
    adresses_list = create_emails_list()
    # loop_list = get_gmails_by_loop(adresses_list)
    # comprehension_result = get_gmails_by_list_comprehension(adresses_list)
    loop_time = timeit.timeit(lambda:get_gmails_by_loop(adresses_list), globals=globals(), number=900000)
    comprehension_time = timeit.timeit(lambda:get_gmails_by_list_comprehension(adresses_list), globals=globals(), number=900000)
    if comprehension_time <= loop_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')

    times = sorted([loop_time, comprehension_time])
    print(f'{times[0]} vs {times[1]}')


if __name__ == '__main__':
    benchmark_work()
