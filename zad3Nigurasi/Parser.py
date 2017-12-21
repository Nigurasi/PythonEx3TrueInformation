import argparse
from zad3Nigurasi.MyExceptions import WrongArgumentException


class ParseArgs:
    def __init__(self):
        self.parser = argparse. \
            ArgumentParser(description='It will help you '
                                       'approximate the truth'
                                       ' of an information.')
        self.arguments = None

    def configure_args(self):
        self.parser. \
            add_argument('--action', '-a', action='store', type=str,
                         dest='action', default='checkBoth',
                         choices=["checkExist",
                                  "checkTruth",
                                  "checkBoth",
                                  "add_to_trusty",
                                  "remove_from_trusty",
                                  "add_to_not_trusty",
                                  "remove_from_not_trusty"],
                         help='A action which will be performed. '
                              'Default = checkBoth')

        self.parser. \
            add_argument('--typeData', '-td', action='store', type=str,
                         dest='type_data', default='equation',
                         choices=['equation', 'url', 'text'],
                         help='Type of data that will be given in data field.'
                              'For queue equation and url is acceptable.'
                              'For add_* only url and text is acceptable.')

        self.parser. \
            add_argument('--data', '-d', action='store', type=str,
                         dest='data',
                         default='Adolf Hitler birthday = 20 April 1889',
                         help='Data that is needed to retrieve the truth. '
                              'The string as default or a link is a '
                              'possible here. In the string left side '
                              'is tags and right side is actual fact.')

        self.parser. \
            add_argument('--pathFile', '-p', action='store', type=str,
                         dest='path_name',
                         default='./Logs/Logger.txt',
                         help='The path for logger file.')

    def get_parsed_arguments_command(self):
        self.configure_args()
        self.arguments = self.parser.parse_args()

        try:
            self.interpret_arguments()
        except WrongArgumentException as e:
            raise e
        return self.arguments

    def get_parsed_arguments_variables(self,
                                       action,
                                       type_data,
                                       data,
                                       logger_name):
        self.configure_args()
        self.arguments = self.parser. \
            parse_args(["-a", action, "-td", type_data,
                        "-d", data, "-p", logger_name])
        try:
            self.interpret_arguments()
        except WrongArgumentException as e:
            raise e
        return self.arguments

    def interpret_arguments(self):
        if "check" in self.arguments.action and \
                (self.arguments.type_data != 'equation' and
                 self.arguments.type_data != 'url'):
            raise WrongArgumentException
        if 'add' in self.arguments.action and \
                (self.arguments.type_data != 'text' and
                 self.arguments.type_data != 'url'):
            raise WrongArgumentException
        if 'remove' in self.arguments.action and \
                (self.arguments.type_data != 'text' and
                 self.arguments.type_data != 'url'):
            raise WrongArgumentException

        if "check" in self.arguments.action \
                and '=' not in self.arguments.data:
            raise WrongArgumentException
