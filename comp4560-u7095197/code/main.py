import numpy as np
import tqdm
from search_weight import SearchWeight
from bias_word_list.bias_word_list import BiasWordList
from bias_checker import BiasChecker
from marco import Marco
from search import Search
from no_bias_query_collection import NoBiasQueryCollection

class BiasInSearchEngines:
    def __init__(self):
        self.search_weight = SearchWeight("data/search_weight.csv")
        self.top_k = self.search_weight.top_k
        print("# Search Weight loading completed")

        self.bias_word_list = BiasWordList()
        print("# Bias WordList loading completed")

        self.bias_checker = BiasChecker()
        print("# Bias Checker loading completed")

        # If all data sets are used, 64g memory will not be enough
        self.marco = Marco("data/ms_marco.tsv", doc_max_num = 1000000) # 1000000
        print("# MS_MARCO loading completed")

        self.search = Search(self.marco, self.top_k)
        print("# Search Engine loading completed")

        self.no_bias_query_collection = NoBiasQueryCollection("data/no_bias_query_collection.csv",
                                                              self.bias_word_list.gender_bias_word_dict,
                                                              self.bias_word_list.location_bias_word_dict)
        print("# No Bias Query Collection loading completed")

        self.scores_bias_gender = None
        self.scores_bias_location = None

    def _calc_one_query(self, query):
        doc_list = self.search.search(query)
        tokenized_doc_list = [i.split(" ") for i in doc_list]

        gender_bias_scores = self._calc_one_(tokenized_doc_list, self.bias_word_list.gender_bias_word_dict)
        location_bias_scores = self._calc_one_(tokenized_doc_list, self.bias_word_list.location_bias_word_dict)

        return gender_bias_scores, location_bias_scores

    def _calc_one_(self, tokenized_doc_list, bias_word_dict):

        scores = np.zeros((self.top_k, len(bias_word_dict.keys())))
        for i in range(self.top_k):
            scores_temp = self.bias_checker.check(tokenized_doc_list[i], bias_word_dict)

            scores[i] = scores_temp

        # search_weight
        scores = np.multiply(scores, self.search_weight.weight)
        scores = np.sum(scores, axis=0)

        bias_score = scores.max() - scores.min()
        return scores


    def calc(self):
        query_num = len(self.no_bias_query_collection.data)

        # init scores ndarray
        scores_all_gender = np.zeros((query_num, len(self.bias_word_list.gender_bias_word_dict.keys())))
        scores_all_location = np.zeros((query_num, len(self.bias_word_list.location_bias_word_dict.keys())))

        print("# Search from Query List")
        for i in tqdm.trange(query_num):
            query = self.no_bias_query_collection.data[i]
            gender_bias_scores, location_bias_scores = self._calc_one_query(query)
            scores_all_gender[i] = gender_bias_scores
            scores_all_location[i] = location_bias_scores

        print("# Complete!")
        self.scores_bias_gender = scores_all_gender.sum(axis=0) / scores_all_gender.sum()
        self.scores_bias_location = scores_all_location.sum(axis=0) / scores_all_location.sum()

        # print gender bias by percent
        print("\n===== Analysis Report =====")
        print("\nGender Bias:")
        for i in range(len(self.bias_word_list.gender_bias_word_dict.keys())):
            print("\t", list(self.bias_word_list.gender_bias_word_dict.keys())[i].title(), '{:.2%}'.format(self.scores_bias_gender[i]))

        # print location bias by percent
        print("\nLocation Bias:")
        for i in range(len(self.bias_word_list.location_bias_word_dict.keys())):
            print("\t", list(self.bias_word_list.location_bias_word_dict.keys())[i].title(), '{:.2%}'.format(self.scores_bias_location[i]))




if __name__ == '__main__':

    print("# Running!")
    bias_in_search_engines = BiasInSearchEngines()
    bias_in_search_engines.calc()


