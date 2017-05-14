def build_dict(file_name) -> dict:
    file = open(file_name, 'r')

    _dict = dict()

    for line in file:
        kv_pair = line.split('->')
        _dict[kv_pair[0]] = kv_pair[1].strip('\n')

    file.close()
    print(_dict)
    return _dict


def check_question(phrase: str, kw_dict: dict) -> str:
    """
    If the keyword is in the phrase, we recognize the question and return that question.
    If not found, then return -1
    """
    for k, v in kw_dict.items():
        if k in phrase:
            return v
    return ''


def save_question(phrase: str, url: str):
    print(phrase)
    print(url)