def general_func():
    import sys

    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if len(sys.argv) != 2:
        print("Usage: python marketing.py [call_center|potential_clients|loyalty_program]")
        sys.exit(1)

    task_name = sys.argv[1].strip()
    clients_set = get_clients_set(clients)
    participants_set = get_participants_set(participants)
    recipients_set = get_recipient_set(recipients)

    if task_name == 'loyalty_program':
        not_participated_list = list(clients_set - participants_set)
        print(sorted(not_participated_list))

    elif task_name == 'potential_clients':
        not_clients_list = list(participants_set - clients_set)
        print(sorted(not_clients_list))

    elif task_name == 'call_center':
        not_promoted_list = list(clients_set - recipients_set)
        print(sorted(not_promoted_list))

    else:
        print('Invalid task name.')
        sys.exit(1)


def get_clients_set(clients):
    return set(clients)


def get_participants_set(participants):
    return set(participants)


def get_recipient_set(recipients):
    return set(recipients)


if __name__ == '__main__':
    general_func()
