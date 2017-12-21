import os

# import pytest
from zad3Nigurasi.Logger import Logger
from zad3Nigurasi.Parser import ParseArgs


def test_init_logger_not_empty_msgs():
    parser = ParseArgs()
    args = parser.get_parsed_arguments_variables("checkBoth",
                                                 "equation",
                                                 "Mark = ",
                                                 "../Logs/Logger.txt")
    logger = Logger(args)
    assert logger.messages


def test_three_msgs_in_logger_after_two_message_methods():
    parser = ParseArgs()
    args = parser.get_parsed_arguments_variables("checkBoth",
                                                 "equation",
                                                 "Mark = ",
                                                 "./Logs/Logger.txt")
    logger = Logger(args)
    logger.other_message("test message")
    logger.other_message("another test message")

    os.remove(logger.path_name)

    assert (len(logger.messages) == 3)


def test_seven_lines_in_file_after_del_init_logger():
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

    os.remove(path)

    assert (len(data.split("\n")) == 8)
