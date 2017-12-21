import sys
import http.client

from zad3Nigurasi.MyExceptions import WrongArgumentException
from zad3Nigurasi.Parser import ParseArgs
from zad3Nigurasi.EquationSolver import EquationSolver
from zad3Nigurasi.Logger import Logger
from zad3Nigurasi.TrustyNotTrustyList import TrustyNotTrustyList


def check_connection(logger):
    conn = http.client.HTTPConnection('www.google.pl')
    try:
        conn.request("HEAD", "/")
        conn.close()
    except Exception as e:
        print("Could not get connected: {0}".format(e))
        logger.exception_message("check_connection",
                                 "Could not get connected: {0}".format(e))
        conn.close()
        sys.exit(1)
    print("Connection checked.")
    logger.other_message("Connection checked.")


def main():
    parser = ParseArgs()

    try:
        arguments = parser.get_parsed_arguments_command()
    except WrongArgumentException as e:
        print(e)
        sys.exit(1)

    logger = Logger(arguments)
    print(arguments)
    action = arguments.action
    data = arguments.data

    check_connection(logger)
    trusty_list = TrustyNotTrustyList("TrustyList.txt", logger)
    not_trusty_list = TrustyNotTrustyList("NotTrustyList.txt", logger)

    if "check" in action:
        equation_solver = EquationSolver(data, action,
                                         logger, trusty_list,
                                         not_trusty_list)
        equation_solver.solve_equation()
    elif action == "add_to_trusty":
        trusty_list.add(data)
    elif action == "remove_from_trusty":
        trusty_list.remove(data)
    elif action == "add_to_not_trusty":
        not_trusty_list.add(data)
    elif action == "remove_from_not_trusty":
        not_trusty_list.remove(data)

    del logger


if __name__ == '__main__':
    main()
