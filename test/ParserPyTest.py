import pytest
from zad3Nigurasi.Parser import ParseArgs
from zad3Nigurasi.MyExceptions import WrongArgumentException


def test_get_parsed_arguments_variables_correct():
    parser = ParseArgs()
    assert (str(parser.
                get_parsed_arguments_variables
                ("checkBoth", "equation", "Mark = ",
                 "./Logs/Logger.txt")) == "Namespace(action='checkBoth', "
            "data='Mark = ', path_name='./Logs/Logger.txt', "
            "type_data='equation')")


def test_get_parsed_arguments_variables_wrong_action():
    parser = ParseArgs()

    with pytest.raises(WrongArgumentException):
        parser.get_parsed_arguments_variables("add_to_trusty",
                                              "equation",
                                              "Mark = true",
                                              "./Logs/Logger.txt")


def test_get_parsed_arguments_variables_wrong_data():
    parser = ParseArgs()

    with pytest.raises(WrongArgumentException):
        parser. \
            get_parsed_arguments_variables("checkBoth",
                                           "equation",
                                           "Mark",
                                           "./Logs/Logger.txt")
