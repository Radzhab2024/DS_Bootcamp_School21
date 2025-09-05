def replace_commas():
    input_file = 'ds.csv'
    output_file = 'ds.tsv'

    with open('ds.csv', 'r', encoding='utf-8') as infile:
        data_strings = infile.readlines()

    with open('ds.tsv', 'w', encoding='utf-8') as outfile:
        for string in data_strings:
            improved_line = replace_correctly(string)
            outfile.write(improved_line + '\n')

def replace_correctly(line):
    result = []
    is_inside_quotes = False

    for char in line:
        if char == '"':
            is_inside_quotes = not is_inside_quotes
            result.append(char)
        elif char == ',' and not is_inside_quotes:
            result.append('\t')
        else:
            result.append(char)
    return ''.join(result).strip()


if __name__ == '__main__':
    replace_commas()
