import unittest
from zad3Nigurasi.TrustyNotTrustyList import TrustyNotTrustyList
from zad3Nigurasi.Parser import ParseArgs
from zad3Nigurasi.Logger import Logger
import os


class TrustyNotTrustyListTest(unittest.TestCase):
    def test_newFileEmptyLists(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)

        trusty_list = TrustyNotTrustyList("TrustyListTest.txt", logger)
        not_trusty_list = TrustyNotTrustyList("NotTrustyListTest.txt", logger)

        t = trusty_list.cur_list
        nt = not_trusty_list.cur_list

        os.remove(trusty_list.path_name)
        os.remove(not_trusty_list.path_name)

        self.assertFalse(t)
        self.assertFalse(nt)

    def test_addedOneElementToEmptyList(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)

        trusty_list = TrustyNotTrustyList("TrustyListTest.txt", logger)
        trusty_list.add("wikipedia")

        cur = trusty_list.cur_list

        os.remove(trusty_list.path_name)

        self.assertTrue(cur)
        self.assertEqual(cur, ["wikipedia"])

    def test_addedSameElementTwice(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)

        trusty_list = TrustyNotTrustyList("TrustyListTest.txt", logger)
        trusty_list.add("wikipedia")
        trusty_list.add("wikipedia")

        cur = trusty_list.cur_list

        os.remove(trusty_list.path_name)

        self.assertTrue(cur)
        self.assertEqual(cur, ["wikipedia"])
        self.assertEqual(len(cur), 1)


if __name__ == '__main__':
    unittest.main()
