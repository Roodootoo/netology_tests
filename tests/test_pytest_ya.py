import pytest
import os
from main import YaUploader


def test_create_folder():
    """Можно делать отдельно функцию без объявления класса тестирования!"""
    with open(os.path.abspath(os.path.join('..', 'token_ya.txt')), 'r') as file_token_ya:
        token_ya = file_token_ya.read().strip()
        ya = YaUploader(token_ya)
        create_result = ya.create_folder()
        assert create_result in (201, 409) # 201 - создана, 209 - существует


