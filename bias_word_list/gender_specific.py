import csv

class GenderSpecific():
    def __init__(self, path):
        self.path = path
        self.data = {}

        self._read_csv()

    # Read from csv and Classified data
    def _read_csv(self):
        temp_list = []

        with open("data/gender_specific_word_list.csv") as f:
            csv_file = csv.reader(f)
            for row in csv_file:
                temp_list.append(row[0])

        self.data["male"] = temp_list[:32]
        self.data["female"] = temp_list[32:]

