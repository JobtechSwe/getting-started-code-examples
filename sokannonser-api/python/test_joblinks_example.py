import requests
import json

"""
Install python packages:
pip install -r requirements.txt

Add your api-key
Add the url to the system you are running the tests against
"""

api_key = ''
url = "http://localhost:5000"

headers = {'api-key': api_key, 'accept': 'application/json'}
url_for_joblinks = f"{url}/joblinks"


def test_search_return_number_of_hits():
    query = 'lärare'
    limit = 0  # limit: 0 means no ads, just a value of how many ads were found
    search_params = {'q': query, 'limit': '0'}
    response = requests.get(url_for_joblinks, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    number_of_hits = json_response['total']['value']


def test_search_loop_through_hits():
    query = 'lärare'
    limit = 100  # 100 is max number of hits that can be returned.
    #  If there are more (which you find with ['total']['value'] in the json response)
    #  you have to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit}
    response = requests.get(url_for_joblinks, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    hits = json_response['hits']
    for hit in hits:
        print(hit['headline'])


def test_download_hits_using_offset():
    """
    This test shows how to use offset to download more than 100 ads (the current limit)
    """
    q = ''  # the search term
    limit = 100  # limit: 100 is the maximum allowed number of hits.
    # Use ['total']['value'] to see the actual number of hits for the query
    search_params = {q: q, 'limit': limit}
    response = requests.get(url_for_joblinks, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    number_of_hits = json_response['total']['value']

    all_headlines = []
    for offset in range(0, number_of_hits, limit):
        response = requests.get(url_for_joblinks, headers=headers, params=search_params)
        json_response = json.loads(response.content.decode('utf8'))
        for hit in json_response['hits']:
            all_headlines.append(hit['headline'])

    for headline in all_headlines:
        print(headline)


if __name__ == '__main__':
    test_search_return_number_of_hits()
    test_search_loop_through_hits()
    test_download_hits_using_offset()
