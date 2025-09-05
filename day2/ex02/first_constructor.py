import sys
import os


class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' not found.")

        with open(self.file_path, 'r') as file:
            read_lines = [line.strip() for line in file if line.strip()]

        if len(read_lines) < 2:
            raise ValueError(f'File must contain a header and at least one data row.')

        header_line = read_lines[0].split(',')

        if len(header_line) != 2:
            raise ValueError(f'Header must contain exactly two columns, separated by a comma.')
        
        valid_data = {'1,0', '0,1'}

        for line in read_lines[1:]:
            if line not in valid_data:
                raise ValueError(f'Invalid data in line: {line}')

        return read_lines



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        file_content = research.file_reader()
        print("\n".join(file_content))
    except Exception as e:
        print(f"Error: {e}")
