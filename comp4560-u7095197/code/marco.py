import codecs

class Marco:
    def __init__(self, file_path, doc_max_num):
        self.file_path = file_path
        self.doc_max_num = doc_max_num
        self.doc = []

        self.tokenized = []

        self._read_tsv()
        self._tokenization()

    def _read_tsv(self):
        with codecs.open(self.file_path, 'r') as f:

            for i in range(self.doc_max_num):
                line = f.readline()
                if len(line) == 0:
                    break
                row = line.rstrip("\r\n").split('\t')
                self.doc.append(row[1])



    def _tokenization(self):
        for doc in self.doc:
            self.tokenized.append(doc.split(" "))
