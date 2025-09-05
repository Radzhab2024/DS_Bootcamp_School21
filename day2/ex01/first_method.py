class Research:
    def file_reader(self):

        with open('data.csv', 'r') as file:
            text_in_file = file.read()
        return text_in_file


if __name__ == '__main__':
    read_text = Research()
    print(read_text.file_reader())
