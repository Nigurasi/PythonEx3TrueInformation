import unittest
from zad3Nigurasi.Parser import ParseArgs
from zad3Nigurasi.MyExceptions import WrongArgumentException


class ParserTest(unittest.TestCase):
    def test_getParsedArgumentsVariablesCorrect(self):
        parser = ParseArgs()
        self.assertEquals(str(parser.
                              get_parsed_arguments_variables
                              ("checkBoth", "equation", "Mark = ",
                               "./Logs/Logger.txt")),
                          "Namespace(action='checkBoth', "
                          "data='Mark = ', path_name='./Logs/Logger.txt', "
                          "type_data='equation')")

    def test_getParsedArgumentsVariablesWrongAction(self):
        parser = ParseArgs()

        with self.assertRaises(WrongArgumentException):
            parser.get_parsed_arguments_variables("add_to_trusty",
                                                  "equation",
                                                  "Mark = true",
                                                  "./Logs/Logger.txt")

    def test_getParsedArgumentsVariablesWrongData(self):
        parser = ParseArgs()

        with self.assertRaises(WrongArgumentException):
            parser.\
                get_parsed_arguments_variables("checkBoth",
                                               "equation",
                                               "Mark",
                                               "./Logs/Logger.txt")


if __name__ == '__main__':
    unittest.main()
