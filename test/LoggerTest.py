import unittest
from zad3Nigurasi.Logger import Logger
from zad3Nigurasi.Parser import ParseArgs


class LoggerTest(unittest.TestCase):
    def test_initLoggerNotEmptyMsgs(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        self.assertTrue(logger.messages)

    def test_threeMsgsInLoggerAfterTwoOtherMessageMethods(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        logger.other_message("test message")
        logger.other_message("another test message")

        self.assertEquals(len(logger.messages), 3)

    def test_sevenLinesInFileAfterDelInitTheLogger(self):
        parser = ParseArgs()
        args = parser.get_parsed_arguments_variables("checkBoth",
                                                     "equation",
                                                     "Mark = ",
                                                     "./Logs/Logger.txt")
        logger = Logger(args)
        path = logger.path_name
        del logger

        with open(path, "r") as f:
            data = f.read()

        self.assertEquals(len(data.split("\n")), 8)


if __name__ == '__main__':
    unittest.main()
