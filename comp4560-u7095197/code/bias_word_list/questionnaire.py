import csv
from collections import defaultdict
import matplotlib.pyplot as plt

# This is a class used to analyze the biased word list questionnaire
class Questionnaire():
    def __init__(self, file_path, name):
        self.file_path = file_path
        self.name = name

        self.data = {}
        self.csv_headers = []
        self.csv_rows = []

        self._read_csv()
        self._data_classification()

    # read result from file
    def _read_csv(self):
        with open(self.file_path) as f:
            csv_file = csv.reader(f)
            self.csv_headers = next(csv_file)
            for row in csv_file:
                self.csv_rows.append(row)

    # Classify the data in CSV. Rank word frequency.
    def _data_classification(self):
        temp_data = {}

        # init headers
        for header in self.csv_headers:
            temp_data[header] = defaultdict(int)
            self.data[header] = []

        # Classify the data and Calculate word frequency
        for row in self.csv_rows:
            for i in range(len(self.csv_headers)):
                temp_data[self.csv_headers[i]][row[i]] += 1

        # Rank word frequency
        for header in temp_data.keys():
            for word in temp_data[header].keys():
                self.data[header].append((word, temp_data[header][word]))

            self.data[header].sort(key=lambda x: (-x[1]))

    def get_word_by_frequency(self):
        res_dic = {}
        for header in self.data.keys():
            words = []
            for word, frequency in self.data[header]:
                words.append(word)

            res_dic[header] = words

        return res_dic


    def output_pdf(self):
        for header in self.data.keys():
            words = []
            frequencies = []
            for word, frequency in self.data[header]:
                words.append(word)
                frequencies.append(frequency)

            plt.figure(figsize=(20, 10))
            plt.bar(words, frequencies)
            plt.title(f"{self.name.title()} Questionnaire Result : {header}", fontdict={'fontsize': 20})
            plt.ylabel("Frequency", fontdict={'fontsize': 15})
            plt.xticks(rotation=90)
            plt.savefig(f'../output/{self.name}_questionnaire_result_{header}.pdf')
            plt.show()
