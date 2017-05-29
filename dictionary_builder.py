def build_dict(file_name) -> dict:
    import csv
    _dict = dict()
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            _dict[row[0]] = row[1]

    return _dict


def check_question(phrase: str, kw_dict: dict) -> str:
    """
    If all keywords in the phrase, we recognize the question and return that question.
    If not found, then return empty
    """
    for k, v in kw_dict.items():
        if all(word in phrase.casefold() for word in k.split('|')):
            return v
    return ''


def save_question(url: str, reason: str, question: str=''):
    import csv
    import datetime
    day = datetime.datetime.now().strftime("%Y-%m-%d")
    with open('../samples/saved_urls_{}'.format(day), 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([url, reason, [question]])



def parse_urls(file_name: str) -> list:
    import csv
    with open(file_name, newline='') as file:
        next(file)
        reader = csv.reader(file, delimiter=',')
        return [row[1] for row in reader]
