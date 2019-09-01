import json
import time
import requests


url_part1 = 'https://api.cognitive.microsoft.com/bing/v5.0/search?q='
url_part2 = '&count=5&offset=0&mkt=en-us&safesearch=Moderate'


def get_content_from_url(item):
    q = ''
    for elem in item:
        q += elem
        q += ' '

    url = url_part1+q+url_part2
    try:
        headers = {'Ocp-Apim-Subscription-Key':
                   'code'}

        r = requests.get(url, headers=headers)
        data = r.text
        # print(r.status_code)
        r.close()
    except Exception as e:
        raise e
    time.sleep(0.15)
    return data


class ApiCheckBing:
    def __init__(self, logger):
        self.logger = logger
        self.snippets = []

    def bing_check_exist(self, combinations):
        for item in combinations:
            try:
                content = get_content_from_url(item)
                json_string = json.loads(content)
                pages = []

                webPages = json_string['webPages']['value']
                for webPage in webPages:
                    webName = webPage['name']
                    display_url = webPage['displayUrl']
                    snippet = webPage['snippet']

                    pages.append((webName, display_url, snippet))

                self.snippets.append((item, pages))
            except Exception as e:
                print(e)
                self.logger.exception_message("bing_check_exist", e)

        for item in self.snippets:
            text = "<ApiCheckBing> Found " \
                   "for combination: {0}:\n".format(item[0])
            for i, web in enumerate(item[1]):
                text += "   Web no. {0}. WebTitle: {1}\n".format(i+1, web[0])
                text += "   Url: {0}\n  Snippet: {1}".format(web[1], web[2])
            self.logger.other_message(text)

    def bing_check_truth(self, combinations_tags,
                         combination_data, trusty_list,
                         not_trusty_list):
        true_texts = []

        if not self.snippets:
            for item in combinations_tags:
                try:
                    content = get_content_from_url(item)
                    json_string = json.loads(content)
                    pages = []

                    webPages = json_string['webPages']['value']
                    for webPage in webPages:
                        webName = webPage['name']
                        display_url = webPage['displayUrl']
                        snippet = webPage['snippet']

                        pages.append((webName, display_url, snippet))

                    self.snippets.append((item, pages))
                except Exception as e:
                    print(e)
                    self.logger.exception_message("bing_check_truth", e)

        for j, data in enumerate(combination_data):
            str_data = data[0]
            if len(data) != 1:
                i = 1
                while i < len(data):
                    str_data += " "
                    str_data += data[i]
                    i += 1
            true_texts.append((str_data, []))

            for i, item in enumerate(self.snippets):
                true_texts[j][1].append((item[0], []))
                for web in item[1]:
                    if str_data in web[2]:
                        true_texts[j][1][i][1].append(web)

        to_logger = "<ApiCheckBing> Found data(with repeated urls):\n"
        for data in true_texts:
            to_logger += "DATA: {0}:\n".format(data[0])
            for tags in data[1]:
                to_logger += "  TAGS {0}:\n".format(tags[0])
                if not tags[1]:
                    to_logger += "      NO FOUND\n"
                for web in tags[1]:
                    if_found_trusty = 0
                    if_found_not_trusty = 0
                    for item in trusty_list:
                        if item in web[1]:
                            if_found_trusty = 1
                            break

                    for item in not_trusty_list:
                        if item in web[1]:
                            if_found_not_trusty = 1
                            break

                    if if_found_trusty:
                        to_logger += "[TRUSTY]"
                    if if_found_not_trusty:
                        to_logger += "[NOT TRUSTY]"
                    to_logger += "      WebName: {0}\n" \
                                 "      Url: {1}\n" \
                                 "      Snippet: {2}\n"\
                        .format(web[0], web[1], web[2])

        # print(to_logger)
        self.logger.other_message(to_logger)
