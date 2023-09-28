from lib.challenge import *
from unittest.mock import Mock

def test_with_mock_api_call():
    mock_requester = Mock()
    mock_requester.get.return_value.json.return_value = {"fact":"A cat usually has about 12 whiskers on each side of its face.","length":61}
    cat_facts = CatFacts(mock_requester)
    assert cat_facts.provide() == "Cat fact: A cat usually has about 12 whiskers on each side of its face."