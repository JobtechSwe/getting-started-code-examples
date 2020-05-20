import requests
import json

"""
Install python packages:
pip install -r requirements.txt

Add your api-key
Add the url to the system you are running the tests against

This file has some examples of how to do filtering on the /stream endpoint
multiple occupations, locations and date can be used

Logic:
[date] AND [occupation 1 OR occupation 2 ...] AND [location 1 OR location 2 ...]

run examples individually with pytest (pip install pytest) or run all of them as 
a Python program: python test_stream_examples

the variable list_of_ads is a list of dictionaries, each ad is a separate dictionary
"""

# your variables:
api_key = ' '
url = "https://     "

headers = {'api-key': api_key, 'accept': 'application/json'}
url_for_stream = f"{url}/stream"


def test_stream_date_from():
    date_from = '2020-01-01T00:00:01'
    filter_params = {'date': date_from}
    list_of_ads = _get_stream_with_params_and_return_list_of_ads(filter_params)
    for ad in list_of_ads:
        print(ad['headline'])


def test_stream_from_date_to_date():
    """
    Use two parameters:

    """
    date_from = '2020-01-01T00:00:01'
    date_to = '2020-05-01T00:00:01'

    filter_params = {'date': date_from, 'updated-before-date': date_to}
    list_of_ads = _get_stream_with_params_and_return_list_of_ads(filter_params)


def test_stream_from_date_and_occupation():
    """
    Use two parameters:
    'date'
    'occupation-concept-id'
    """

    date_from = '2020-01-01T00:00:01'

    # 'occupation-concept-id'
    systemutvecklare_programmerare = "fg7B_yov_smw"

    filter_params = {'date': date_from, 'occupation-concept-id': systemutvecklare_programmerare}
    list_of_ads = _get_stream_with_params_and_return_list_of_ads(filter_params)


def test_stream_from_date_and_location():
    """
    Use two parameters:
    'date'
    'location-concept-id'
    """
    date_from = '2020-01-01T00:00:01'
    # 'location-concept-id'
    uppsala_lan = "zBon_eET_fFU"

    filter_params = {'date': date_from, 'location-concept-id': uppsala_lan}
    list_of_ads = _get_stream_with_params_and_return_list_of_ads(filter_params)


def test_stream_from_date_and_occupation_and_location():
    """
    Use three parameters:
    'date'
    'location-concept-id'
    'occupation-concept-id'
    """
    date_from = '2020-01-01T00:00:01'
    # 'location-concept-id'
    skane_lan = "CaRE_1nn_cSU"
    # 'occupation-concept-id'
    personlig_assistent = "eU1q_zvL_9Rf"

    filter_params = {'date': date_from, 'occupation-concept-id': personlig_assistent, 'location-concept-id': skane_lan}
    list_of_ads = _get_stream_with_params_and_return_list_of_ads(filter_params)


def _get_stream_with_params_and_return_list_of_ads(filter_params):
    """
    This function handles:
        http GET request
        check that no http error is returned
        converting the bytestring in the response to a list of ads
    """
    response = requests.get(url_for_stream, headers=headers, params=filter_params)
    response.raise_for_status()  # check for http errors
    list_of_ads = json.loads(response.content.decode('utf8'))
    return list_of_ads


if __name__ == '__main__':
    test_stream_date_from()
    test_stream_from_date_to_date()
    test_stream_from_date_and_occupation()
    test_stream_from_date_and_location()
    test_stream_from_date_and_occupation_and_location()
