from __future__ import print_function

import requests
import urllib
import yaml

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

GRANT_TYPE = 'client_credentials'


def load_api_key(filename='yelp_api_key.yaml'):
    """Load Yelp API client ID and client secret and return them as a dictionary."""
    with open(filename) as f:
        return yaml.load(f)


def obtain_bearer_token(host, path, key):
    """Obtain a bearer token by sending a POST request with user's API keys to the API.

    Parameters
    ----------
    host : str
        The domain host of the API.
    path : str
        The path of the API after the domain.
    key : dict
        A dictionary containing values for client_id and client_secret.

    Returns
    -------
    str
        OAuth bearer token, obtained using client_id and client_secret.

    Raises
    ------
    HTTPError
        An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    CLIENT_ID = key['client_id']
    CLIENT_SECRET = key['client_secret']
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.

    Parameters
    ----------
    host : str
        The domain host of the API.
    path : str
        The path of the API after the domain.
    bearer_token : str
        OAuth bearer token, obtained using client_id and client_secret.
    url_params : dict
        An optional set of query parameters in the request.

    Returns
    -------
    dict
        The JSON response from the request.

    Raises
    ------
    HTTPError
        An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()
