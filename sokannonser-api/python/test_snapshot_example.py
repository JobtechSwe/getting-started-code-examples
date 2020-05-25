import requests
import json

"""
Install python packages:
pip install -r requirements.txt

Add your api-key
Add the url to the system you are running the tests against

 /snapshot will return all ads

the variable list_of_ads is a list of dictionaries, each ad is a separate dictionary
"""

# your variables:
api_key = ' '
url = "https://       "

headers = {'api-key': api_key, 'accept': 'application/json'}
url_for_snapshot = f"{url}/snapshot"


def test_get_snapshot():
    response = requests.get(url_for_snapshot, headers=headers)
    response.raise_for_status()  # check for http errors
    list_of_ads = json.loads(response.content.decode('utf8'))


if __name__ == '__main__':
    test_get_snapshot()
