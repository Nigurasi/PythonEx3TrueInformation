import unittest
from zad3Nigurasi.EquationSolver import EquationSolver
from zad3Nigurasi.Logger import Logger
from zad3Nigurasi.Parser import ParseArgs
from zad3Nigurasi.TrustyNotTrustyList import TrustyNotTrustyList


class LoggerTest(unittest.TestCase):
    def test_initCorrectData(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation", "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        trusty_list = TrustyNotTrustyList("TrustyList.txt", logger)
        not_trusty_list = TrustyNotTrustyList("NotTrustyList.txt", logger)

        es = EquationSolver("Mark = ", "checkBoth",
                            logger, trusty_list,
                            not_trusty_list)

        self.assertEqual(es.logger, logger)
        self.assertEqual(es.trusty_list, trusty_list.cur_list)
        self.assertEqual(es.not_trusty_list, not_trusty_list.cur_list)
        self.assertEqual(es.action, 'checkBoth')
        self.assertEqual(es.tags, ["Mark"])
        self.assertEqual(es.check_data, [])

    def test_getAllCombinationsEmptyTags(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation", "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        trusty_list = TrustyNotTrustyList("TrustyList.txt", logger)
        not_trusty_list = TrustyNotTrustyList("NotTrustyList.txt", logger)

        es = EquationSolver("Mark = ", "checkBoth",
                            logger, trusty_list,
                            not_trusty_list)

        tags = es.get_all_combinations([])

        self.assertFalse(tags)

    def test_getAllCombinationsCorrect(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation", "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        trusty_list = TrustyNotTrustyList("TrustyList.txt", logger)
        not_trusty_list = TrustyNotTrustyList("NotTrustyList.txt", logger)

        es = EquationSolver("Mark = ", "checkBoth",
                            logger, trusty_list,
                            not_trusty_list)

        tags = es.get_all_combinations(["Mark", "Twain"])

        self.assertTrue(tags)
        self.assertEqual(tags, [("Mark",), ("Twain",),
                                ("Mark", "Twain"),
                                ("Twain", "Mark")])
        self.assertEqual(len(tags), 4)

    def test_getAllCombinationsWithoutPermutation(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation", "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        trusty_list = TrustyNotTrustyList("TrustyList.txt", logger)
        not_trusty_list = TrustyNotTrustyList("NotTrustyList.txt", logger)

        es = EquationSolver("Mark = ", "checkBoth",
                            logger, trusty_list,
                            not_trusty_list)

        tags = es.get_all_combinations_without_permutation(["Mark", "Twain"])

        self.assertTrue(tags)
        self.assertEqual(tags, [("Mark",), ("Twain",), ("Mark", "Twain")])
        self.assertEqual(len(tags), 3)


if __name__ == '__main__':
    unittest.main()
