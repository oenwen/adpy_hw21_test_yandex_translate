import requests
from adpy21_tests_hw2 import data
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

# API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
# URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def get_params(text, to_lang):
    params = {
        'key': data.API_KEY,
        'text': text,
        'lang': 'ru-{}'.format(to_lang),
    }
    return params

def translate_it():
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    text = input('Введите текст на русском языке ')
    response = requests.get(data.URL, params = get_params(text, 'en'))
    return response

def print_translation():
    response = translate_it()
    response_json = response.json()
    return ''.join(response_json['text'])


# print(translate_it('В настоящее время доступна единственная опция —
# признак включения в ответ автоматически определенного языка переводимого текста.
# Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(print_translation())