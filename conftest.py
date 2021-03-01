import pytest
from src.helper import json_parser

@pytest.fixture()
def url_config():
    config = json_parser('url_config.json')
    yield config

@pytest.fixture()
def post_response():
    resp = json_parser('tests/posts_response.json')
    yield resp

@pytest.fixture()
def comments_response():
    resp = json_parser('tests/comments_response.json')
    yield resp