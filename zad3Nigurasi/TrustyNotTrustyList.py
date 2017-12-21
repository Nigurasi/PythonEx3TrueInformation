import os.path


class TrustyNotTrustyList:
    def __init__(self, path_name, logger):
        self.logger = logger
        data = ""
        self.cur_list = []
        if not os.path.exists("Lists"):
            os.makedirs("Lists")

        self.path_name = "./Lists/" + path_name

        if not os.path.isfile(self.path_name):
            text = "Not found the list, so creating with name: {0}"\
                .format(self.path_name)
            logger.other_message(text)
            print(text)
            with open(self.path_name, "w+", encoding='utf-8'):
                pass
        else:
            text = "Found the list with name: {0}".format(self.path_name)
            logger.other_message(text)
            with open(self.path_name, "r", encoding='utf-8') as f:
                data = f.read()
            self.cur_list = data.split("\n")
            self.cur_list.remove("")
            # print(self.cur_list)

    def add(self, data):
        text = data + "\n"
        if data in self.cur_list:
            to_logger = "The data {0} is currently in the {1}."\
                .format(data, self.path_name)
            print(to_logger)
            self.logger.other_message(to_logger)
        else:
            to_logger = "The data {0} was added to {1}."\
                .format(data, self.path_name)
            print(to_logger)
            self.logger.other_message(to_logger)
            self.cur_list.append(data)

            with open(self.path_name, "a", encoding='utf-8') as f:
                f.write(text)

    def remove(self, data):
        if data not in self.cur_list:
            to_logger = "There is no data {0} in the trustyList."\
                .format(data)
            print(to_logger)
            self.logger.other_message(to_logger)
        else:
            to_logger = "The data {0} was " \
                        "removed from TrustyList."\
                .format(data)
            print(to_logger)
            self.logger.other_message(to_logger)

            self.cur_list.remove(data)
            self.cur_list.remove(self.cur_list[len(self.cur_list)-1])

            text = ""
            for item in self.cur_list:
                text = text + item + "\n"

            with open(self.path_name, "w+", encoding='utf-8') as f:
                f.write(text)
