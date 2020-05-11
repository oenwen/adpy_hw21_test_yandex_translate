import unittest
from unittest.mock import patch
from adpy21_tests_hw2 import yandex_translate, data

class TestYandexApi(unittest.TestCase):
    def setUp(self):
        self.api = data.API_KEY
        self.url = data.URL

    def test_response_code(self):
        with patch('adpy21_tests_hw2.yandex_translate.input', return_value = 'привет'):
            response = yandex_translate.translate_it()
            self.assertEqual(response.status_code, 200)

    def test_translation(self):
        with patch('adpy21_tests_hw2.yandex_translate.input', return_value = 'привет'):
            target = yandex_translate.print_translation()
            self.assertEqual(target, 'hi')

    def test_wrong_api(self):
        with patch('adpy21_tests_hw2.yandex_translate.get_params', return_value = {
                'key': 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e',
                'text': 'привет',
                'lang': 'ru-{}'.format('en'),
            }
        ):
            with patch('adpy21_tests_hw2.yandex_translate.input', return_value='привет'):
                response = yandex_translate.translate_it()
        self.assertEqual(response.status_code, 403)


if __name__ == '__main__':
    unittest.main()
