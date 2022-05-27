import math
import numpy as np


class BiasChecker:
    def __init__(self):
        pass

    def check(self, tokenized_doc, word_dict):
        category_list = list(word_dict.keys())
        bias_score = np.zeros(len(category_list))

        for i in range(len(category_list)):
            bias_score[i] = self._calc(tokenized_doc, word_dict[category_list[i]])

        return bias_score

    def _calc(self, tokenized_doc, bias_list):
        res = 0.0
        num_doc = len(tokenized_doc)

        k = len(bias_list)
        coeff = math.e / math.pow(1 / k + 1, k)

        for bias_word in bias_list:
            num_bias_word = tokenized_doc.count(bias_word)
            res += math.log(num_bias_word / num_doc + 1)

        return res * coeff

