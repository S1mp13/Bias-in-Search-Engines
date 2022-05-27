import csv
from bias_word_list.bias_word_list import BiasWordList


class NoBiasQueryCollection:
    def __init__(self, file_path, *bias_dict_list):
        self.file_path = file_path
        self.data = []

        self.bias_word_list = []
        for bias_dict in bias_dict_list:
            for category in bias_dict.keys():
                self.bias_word_list.extend(bias_dict[category])

        self._read_csv()

    def _read_csv(self):
        with open(self.file_path) as f:
            csv_file = csv.reader(f)
            self.csv_headers = next(csv_file)
            for row in csv_file:
                query = row[0]
                if self._check_bias(query):
                    continue
                self.data.append(query)

    def _check_bias(self, query):
        for word in self.bias_word_list:
            if word in query:
                return True
        return False