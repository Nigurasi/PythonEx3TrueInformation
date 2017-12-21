# library which supports python 2 and 3 compatibility
from six.moves.urllib.request import urlopen
import json

months = ["january", "february", "march", "april", "may",
          "june", "july", "august", "september", "october",
          "november", "december"]

wikipedia_url = 'https://en.wikipedia.org/w/api.php?format=json&' \
                'action=query&prop=extracts&exlimit=max&' \
                'explaintext&exintro&titles='


def get_content_from_url(item):
    uri = ''
    for elem in item:
        uri += elem
        uri += '+'
    response = urlopen(wikipedia_url + uri)
    content = response.read().decode('utf-8')
    return content


class ApiCheckWikipedia:
    def __init__(self, logger):
        self.logger = logger
        self.valid_combinations = []

    def wikipedia_check_exist(self, combinations):
        invalid_combinations = []
        valid_combinations = []
        for item in combinations:
            content = get_content_from_url(item)
            try:
                json_string = json.loads(content)
                pageid = list(json_string['query']['pages'].keys())[0]

                if pageid == '-1' or \
                   json_string['query']['pages'][pageid]['extract'] == "":
                    invalid_combinations.append(item)
                else:
                    text = "<ApiCheckWikipedia>  " \
                           "CHANGED FROM: {0} TO: {1} \nTEXT: {2}" \
                        .format(json_string['query']['normalized'][0]['from'],
                                json_string['query']['normalized'][0]['to'],
                                json_string['query']['pages']
                                [pageid]['extract'])

                    self.logger.other_message(text)
                    valid_combinations.append(item)
            except(ValueError, KeyError, TypeError) as e:
                print(e)
                self.logger.exception_message("wikipedia_check_exist", e)

        self.logger.other_message("<ApiCheckWikipedia>  "
                                  "Invalid combinations: {0}."
                                  .format(invalid_combinations))

        self.valid_combinations = valid_combinations
        self.logger.other_message("<ApiCheckWikipedia>  "
                                  "Valid combinations: {0}."
                                  .format(valid_combinations))

    def wikipedia_check_truth(self, combinations_tags, combination_data):
        texts = []
        if not self.valid_combinations:
            for item in combinations_tags:
                content = get_content_from_url(item)
                try:
                    json_string = json.loads(content)
                    pageid = list(json_string['query']['pages'].keys())[0]

                    if pageid != '-1' and \
                       json_string['query']['pages'][pageid]['extract'] != "":
                        text = json_string['query']['pages'][pageid]['extract']
                        texts.append(text)

                except(ValueError, KeyError, TypeError) as e:
                    print(e)
                    self.logger.exception_message("wikipedia_check_truth", e)
        else:
            for item in self.valid_combinations:
                content = get_content_from_url(item)

                json_string = json.loads(content)
                pageid = list(json_string['query']['pages'].keys())[0]
                text = json_string['query']['pages'][pageid]['extract']
                texts.append(text)

        to_logger = "<ApiCheckWikipedia> " \
                    "Found this text matching the pattern:\n"
        for data in combination_data:
            extracts = []
            str_data = data[0]
            if len(data) != 1:
                i = 1
                while i < len(data):
                    str_data += " "
                    str_data += data[i]
                    i += 1
            to_logger += "DATA: {0}:\n".format(str.upper(str_data))

            for i, text in enumerate(texts):
                if str_data in text:
                    offset = text.find(str_data)
                    while offset != -1:
                        end = text.find(".", offset) + 1
                        if end == 0:
                            end = len(text)-1
                        if offset < 40:
                            extract = text[:end]
                        else:
                            extract = text[text.find(" ", offset - 40) + 1:
                                           end]
                        offset = text.find(str_data, offset + 1)

                        extracts.append(extract)
                        to_logger += "TAGS {0}:\n    {1}\n".\
                            format(self.valid_combinations[i], extract)

        # print(to_logger)
        self.logger.other_message(to_logger)
