from bias_word_list.questionnaire import Questionnaire
from bias_word_list.gender_specific import GenderSpecific
from bias_word_list.basic_location import BasicLocation

class BiasWordList:
    def __init__(self):
        # Gender Specific Word List
        self.gender_specific = GenderSpecific("data/gender_specific_word_list.csv")

        # Impression Gender Bias Word List
        self.gender_questionnaire = Questionnaire("data/questionnaire_gender.csv", "gender")
        # self.gender_questionnaire.output_pdf()

        # Gender Bias Word List = Gender Specific Word List + Impression Gender Bias Word List
        self.gender_bias_word_dict = {}

        self._gender_bias_word_dict()

        # ------------------------------

        # Basic Location Word List
        self.basic_location = BasicLocation("data/countries.csv")

        # Impression Location Bias Word List
        self.location_questionnaire = Questionnaire("data/questionnaire_location.csv", "location")
        # self.location_questionnaire.output_pdf()

        # Gender Bias Word List = Gender Specific Word List + Impression Gender Bias Word List
        self.location_bias_word_dict = {}

        self._location_bias_word_dict()

    def _impression_gender_bias_word_dict(self):
        impression_gender_bias_word_dict = {"male": [], "female": []}
        for category in impression_gender_bias_word_dict.keys():
            counter = 0
            for word in self.gender_questionnaire.get_word_by_frequency()[category]:

                if word not in self.gender_specific.data[category]:
                    counter += 1
                    impression_gender_bias_word_dict[category].append(word)

                if counter == 10:
                    break
        return impression_gender_bias_word_dict

    def _gender_bias_word_dict(self):
        impression_gender_bias_word_dict = self._impression_gender_bias_word_dict()
        for category in impression_gender_bias_word_dict.keys():
            self.gender_bias_word_dict[category] = []
            self.gender_bias_word_dict[category].extend(self.gender_specific.data[category])
            self.gender_bias_word_dict[category].extend(impression_gender_bias_word_dict[category])

    def _impression_location_bias_word_dict(self):
        impression_location_bias_word_dict = {"Europe": [], "Asia": [], "America": [], "Oceania": [], "Africa": []}
        for continent in impression_location_bias_word_dict.keys():
            counter = 0
            for word in self.location_questionnaire.get_word_by_frequency()[continent]:

                if word not in self.basic_location.data[continent]["total"]:
                    counter += 1
                    impression_location_bias_word_dict[continent].append(word)

                if counter == 10:
                    break

        return impression_location_bias_word_dict

    def _location_bias_word_dict(self):
        impression_location_bias_word_dict = self._impression_location_bias_word_dict()
        for continent in impression_location_bias_word_dict.keys():
            self.location_bias_word_dict[continent] = []
            self.location_bias_word_dict[continent].extend(self.basic_location.data[continent]["total"])
            self.location_bias_word_dict[continent].extend(impression_location_bias_word_dict[continent])




