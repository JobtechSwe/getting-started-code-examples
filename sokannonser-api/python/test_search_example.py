import requests
import json

"""
Install python packages:
pip install -r requirements.txt

Add your api-key
Add the url to the system you are running the tests against
"""

api_key = ''
url = "https://"

headers = {'api-key': api_key, 'accept': 'application/json'}
url_for_search = f"{url}/search"


def test_search_return_number_of_hits():
    query = 'lärare'
    limit = 0  # limit: 0 means no ads, just a value of how many ads were found
    search_params = {'q': query, 'limit': '0'}
    response = requests.get(url_for_search, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    number_of_hits = json_response['total']['value']


def test_search_loop_through_hits():
    query = 'lärare'
    limit = 100     # 100 is max number of hits that can be returned.
    # If there are more (which you find with 'limit' : 0 ) you have to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit}
    response = requests.get(url_for_search, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    hits = json_response['hits']
    for hit in hits:
        print(hit['headline'])


if __name__ == '__main__':
    test_search_return_number_of_hits()
    test_search_loop_through_hits()
