import unittest
from unittest.mock import patch
from app import get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc, show_all_docs_info
from parameterized import parameterized


class TestFunction(unittest.TestCase):

    @parameterized.expand(
        [
            ('123', True),
            ('2207 876234', True),
            ('11-2', True)
        ]
    )
    @patch('app.user_doc_number')
    def test_get_doc_owner_name(self, user_doc_number_mock, result):
        user_result = get_doc_owner_name()
        self.assertTrue(user_result)

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        self.assertIsInstance(result, list)

    @parameterized.expand(
        [
            ('1', True),
            ('5', True),
            ('7', True)
        ]
    )
    def test_add_new_shelf(self, shelf_number, result):
        n_shelf, user_result = add_new_shelf(shelf_number)
        self.assertTrue(user_result)

    @patch('app.user_doc_number')
    def test_delete_doc(self, user_doc_number_mock):
        user_doc_number_mock = '10006'
        n_doc, result = delete_doc(user_doc_number_mock)
        self.assertTrue(result)

    def test_show_all_docs_info(self):
        result = show_all_docs_info()
        self.assertIsInstance(result, list)
