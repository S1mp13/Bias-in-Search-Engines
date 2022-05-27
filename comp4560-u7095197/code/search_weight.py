import numpy as np
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

class SearchWeight():
    def __init__(self, file_path):
        self.file_path = file_path

        self.csv_rows = []
        self.csv_headers = []

        self.weight = None
        self.top_k = 0

        self._read_csv()
        self._get_top_k()
        self.get_weight()


    def _get_top_k(self):
        self.top_k = max(self.csv_rows)

    def get_weight(self):
        self.weight = np.zeros((self.top_k, 1))
        for i in self.csv_rows:
            self.weight[:i] += 1

        self.weight /= self.weight.sum()

    def _read_csv(self):
        with open(self.file_path) as f:
            csv_file = csv.reader(f)
            self.csv_headers = next(csv_file)

            for row in csv_file:
                self.csv_rows.append(int(row[0]))

    def output_pdf(self):
        pie_dict = defaultdict(int)
        for row in self.csv_rows:
            pie_dict[row] += 1

        x = []
        y = []
        for item_num in pie_dict.keys():
            x.append(pie_dict[item_num])
            y.append(item_num)

        plt.figure(figsize=(15, 15))

        plt.pie(x=x,
                labels=y,
                autopct='%.2f%%',
                textprops={'fontsize': 20, 'color': 'black'}
                )

        plt.title(f"Search Engines Questionnaire Result", fontdict={'fontsize': 20})
        plt.savefig(f'output/search_engines_questionnaire_result.pdf')
        plt.show()
