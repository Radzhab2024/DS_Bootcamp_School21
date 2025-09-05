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


def get_gmails_by_map(emails_list):
    return map(lambda email: email if email.endswith('@gmail.com') else None, emails_list)


def benchmark_work():
    adresses_list = create_emails_list()
    loop_time = timeit.timeit(lambda: get_gmails_by_loop(adresses_list), globals=globals(), number=900000)
    comprehension_time = timeit.timeit(lambda: get_gmails_by_list_comprehension(adresses_list), globals=globals(),
                                       number=900000)
    map_time = timeit.timeit(lambda: get_gmails_by_map(adresses_list), globals=globals(), number=900000)

    results = {
        'loop': loop_time,
        'list comprehension': comprehension_time,
        'map': map_time
    }

    key_of_min_value = min(results, key=results.get)
    print(f'It is better to use a {key_of_min_value}')

    times = sorted([loop_time, comprehension_time, map_time])
    print(f'{times[0]} vs {times[1]} vs {times[2]}')


if __name__ == '__main__':
    benchmark_work()
