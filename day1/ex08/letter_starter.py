def find_employer_and_welcome():
    import sys
    if len(sys.argv) == 2:
        email = sys.argv[1]
        found_name = find_first_name(email)
    else:
        return

    if found_name:
        print(generate_paragraph(found_name))
    else:
        print(f'Employer with email: {email} does not exist')


def find_first_name(email, file_tsv="employees.tsv"):
    try:
        with open(file_tsv, "r") as file:
            lines = file.readlines()

        for line in lines[1:]:
            employer_name, employer_surname, employer_email = line.strip().split("\t")
            if employer_email == email:
                return employer_name

    except FileNotFoundError:
        print(f"Error: The file {file_tsv} does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


def generate_paragraph(first_name):
    return (f'Уважаемый {first_name}, добро пожаловать в нашу команду.\n'
            f'Мы уверены, что нам будет приятно работать с вами.\n'
            f'Это обязательное условие для профессионалов, которых нанимает наша компания.')


if __name__ == '__main__':
    find_employer_and_welcome()
