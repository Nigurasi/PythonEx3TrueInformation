from datetime import datetime
import os.path


def get_cur_time():
    return str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class Logger:
    def __init__(self, arguments):
        self.messages = []
        self.init_message(arguments)

    def __del__(self):
        print("Destructor for Logger")
        msg = "<Class: Logger> Destructing."
        self.other_message(msg)
        self.add_to_logger()

    def init_message(self, arguments):
        cur_time = get_cur_time()
        text = "Programme started with arguments:" \
               "\n    action = {0}\n    typeData = {1}" \
               "\n    data = {2}\n    pathFile = {3}".\
            format(arguments.action, arguments.type_data,
                   arguments.data, arguments.path_name)

        self.path_name = arguments.path_name
        self.add_message(cur_time, text)

    def exception_message(self, fname, exception):
        cur_time = get_cur_time()
        text = "<{0}> An exception has occurred with a " \
               "message: {1}".format(fname, exception)

        self.add_message(cur_time, text)

    def end_message(self):
        cur_time = get_cur_time()
        text = "Programme ended."

        self.add_message(cur_time, text)

    def other_message(self, text):
        cur_time = get_cur_time()

        self.add_message(cur_time, text)

    def generate_data_from_messages(self):
        data = ""
        for item in self.messages:
            data += item
        return data

    def add_to_logger(self):
        self.end_message()
        data = self.generate_data_from_messages()
        if not os.path.exists("Logs"):
            os.makedirs("Logs")

        if ".txt" not in self.path_name:
            self.path_name += ".txt"

        with open(self.path_name, "w+", encoding='utf-8') as f:
            f.write(data)

        print("Everything wrote in logger.\n")

    def add_message(self, cur_time, text):
        message = "<{0}>: {1}\n".format(cur_time, text)
        self.messages.append(message)
