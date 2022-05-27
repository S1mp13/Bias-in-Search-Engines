from marco import Marco
from reference.rank_bm25 import BM25Okapi

class Search:
    def __init__(self, marco, top_k):
        self.top_k = top_k

        self.marco = marco
        self.bm25 = BM25Okapi(self.marco.tokenized)

    def search(self, query):
        tokenized_query = query.split(" ")
        scores = self.bm25.get_scores(tokenized_query)

        temp = []
        for i in range(len(scores)):
            temp.append((scores[i], self.marco.doc[i]))
        temp.sort(key=lambda x: (-x[0]))

        res = []
        for row in temp[:self.top_k]:
            res.append(row[1])

        return res
