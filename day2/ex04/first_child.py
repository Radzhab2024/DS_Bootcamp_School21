import sys
import os
from random import randint

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' not found.")

        with open(self.file_path, 'r') as file:
            read_lines = [line.strip() for line in file if line.strip()]

        if len(read_lines) < 2 and has_header:
            raise ValueError(f'File must contain a header and at least one data row.')

        if has_header:
            read_lines = read_lines[1:]

        valid_data = {'1,0', '0,1'}

        data = []

        for line in read_lines:
            if line not in valid_data:
                raise ValueError(f'Invalid data in line: {line}')
            data.append(list(map(int, line.split(','))))
        return data

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0, 0
            heads_percents = (heads / total) * 100
            tails_percents = (tails / total) * 100

            return heads_percents, tails_percents

    class Analytics(Calculations):

        def predict_random(self, num_of_predictions):
            predictions = []
            for _ in range(num_of_predictions):
                first = randint(0, 1)
                predictions.append([first, 1 - first])
            return predictions

        def predict_last(self):
            if not self.data:
                raise ValueError("No data available to predict the last item.")
            return self.data[-1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    try:
        research = Research(path_to_file)
        file_content = research.file_reader()
        print(file_content)

        analytics = Research.Analytics(file_content)
        heads_sum, tails_sum = analytics.counts()
        print(heads_sum, tails_sum)

        heads_percentage, tails_percentage = analytics.fractions(heads_sum, tails_sum)
        print(heads_percentage, tails_percentage)

        predictions = analytics.predict_random(3)
        print(predictions)

        last_item = analytics.predict_last()
        print(last_item)

    except Exception as e:
        print(f"Error: {e}")