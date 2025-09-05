def get_input_file_name():
    import sys
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        extract_names(input_file)
    else:
        return


def extract_names(inp_file, output_file="employees.tsv"):
    try:
        with open(inp_file, 'r') as file:
            emails = file.read().strip().split('\n')

        with open(output_file, 'w') as file_tsv:
            file_tsv.write(f'Name\tSurname\tE-mail\n')
            for index, email in enumerate(emails):
                names_array = email.split('@')[0].split('.')
                employer_name = names_array[0].capitalize()
                employer_surname = names_array[1].capitalize()

                if index > 0:
                    file_tsv.write('\n')

                file_tsv.write(f'{employer_name}\t{employer_surname}\t{email}')
    except FileNotFoundError:
        print(f"Error: The file {inp_file} does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    get_input_file_name()
