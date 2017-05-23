def build_dict(file_name) -> dict:
    file = open(file_name, 'r')

    _dict = dict()

    for line in file:
        kv_pair = line.split('->')
        _dict[kv_pair[0]] = kv_pair[1].strip('\n')

    file.close()
    return _dict


def check_question(phrase: str, kw_dict: dict) -> str:
    """
    If the keyword is in the phrase, we recognize the question and return that question.
    If not found, then return -1
    """
    for k, v in kw_dict.items():
        if k in phrase.casefold():
            return v
    return ''


def save_question(url: str, reason: str, phrase: str=''):
    import csv
    with open('../samples/saved_urls', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([url, reason, phrase])


def parse_csv(file_name: str):
    import csv
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        return [row[1] for row in reader]
