import itertools
from zad3Nigurasi.ApiCheckWikipedia import ApiCheckWikipedia
from zad3Nigurasi.ApiCheckBing import ApiCheckBing


class EquationSolver:
    def __init__(self, data, action, logger, trusty_list, not_trusty_list):
        self.logger = logger
        datas = data.split('=')
        self.tags = datas[0].split()
        self.check_data = datas[1].split()
        self.action = action
        self.all_combinations_tags = []
        self.trusty_list = trusty_list.cur_list
        self.not_trusty_list = not_trusty_list.cur_list

        self.all_combinations_data = self. \
            get_all_combinations_without_permutation(self.check_data)

    def solve_equation(self):
        self.wikipedia = ApiCheckWikipedia(self.logger)
        self.bing = ApiCheckBing(self.logger)
        if self.action == "checkExist":
            self.check_existence()
        elif self.action == "checkTruth":
            self.check_truth()
        else:
            self.check_existence()
            self.check_truth()

    def check_existence(self):
        self.all_combinations_tags = self.get_all_combinations(self.tags)
        self.wikipedia.wikipedia_check_exist(self.all_combinations_tags)

        self.all_combinations_tags = self.\
            get_all_combinations_without_permutation(self.tags)
        self.bing.bing_check_exist(self.all_combinations_tags)

    def check_truth(self):
        self.all_combinations_tags = self.get_all_combinations(self.tags)
        self.wikipedia.wikipedia_check_truth(self.all_combinations_tags,
                                             self.all_combinations_data)

        self.all_combinations_tags = self.\
            get_all_combinations_without_permutation(self.tags)
        self.bing.bing_check_truth(self.all_combinations_tags,
                                   self.all_combinations_data,
                                   self.trusty_list, self.not_trusty_list)

    def get_all_combinations(self, tags):
        all_combination = []

        for i in range(1, len(tags) + 1):
            for c in itertools.permutations(tags, i):
                all_combination.append(c)

        # print(all_combination)
        self.logger.other_message("Generate all combinations"
                                  " for these tags. :\n    {0}"
                                  .format(all_combination))
        return all_combination

    def get_all_combinations_without_permutation(self, tags):
        all_combination = []

        for i in range(1, len(tags) + 1):
            for c in itertools.combinations(tags, i):
                all_combination.append(c)

        # print(all_combination)
        self.logger.other_message("Generate all combinations"
                                  " for these tags. :\n    {0}"
                                  .format(all_combination))
        return all_combination
