import csv

class BasicLocation:
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.csv_headers = []
        self.csv_row = []

        self._read_csv()
        self._data_classification()

    # Read from csv and Classified data
    def _read_csv(self):
        with open(self.path) as f:
            csv_file = csv.reader(f)
            self.csv_headers = next(csv_file)
            for row in csv_file:
                self.csv_row.append(row)

    # Classify the data in CSV.
    def _data_classification(self):

        # Init continent
        for row in self.csv_row:
            self.data[row[1]] = {}

            for header in self.csv_headers:
                if header == "continent":
                    continue
                self.data[row[1]][header] = []

        # Classify data
        for row in self.csv_row:

            for i in range(len(self.csv_headers)):
                header = self.csv_headers[i]
                if header == "continent":
                    continue
                if row[i] not in self.data[row[1]][header] and len(row[i]) != 0:
                    self.data[row[1]][header].append(row[i])


        for continent in self.data:
            if continent == "total":
                continue
            total = []
            for category in self.data[continent]:
                total.extend(self.data[continent][category])

            self.data[continent]["total"] = total
