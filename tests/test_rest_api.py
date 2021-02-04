import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():

    #Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    #Act
    response = requests.get(url)
    body = response.json()

    #Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api_will_fail():

    #Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    #Act
    response = requests.get(url)
    body = response.json()

    #Assert
    assert response.status_code == 200
    assert 'Pythonsss' in body['AbstractText']