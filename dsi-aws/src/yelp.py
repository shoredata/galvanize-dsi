from timeit import Timer
from yelp_helpers import obtain_bearer_token
from yelp_helpers import request
from yelp_helpers import load_api_key
from pymongo import MongoClient
import multiprocessing
import threading

key = load_api_key()

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
BEARER_TOKEN = obtain_bearer_token(API_HOST, TOKEN_PATH, key)

DB_NAME = "yelp"
COLLECTION_NAME = "business"
client = MongoClient()
db = client[DB_NAME]
coll = db[COLLECTION_NAME]


POOL_SIZE = 4
SEARCH_LIMIT = 20


def city_search_parallel(city):
    """
    Retrieves the JSON response that contains the top 20 business meta data for city.
    :param city: city name
    """
    pass


def business_info_concurrent(ids):
    """
    Extracts the business ids from the JSON object and
    retrieves the business data for each id concurrently.
    :param json_response: JSON response from the search API.
    """
    pass


def scrape_parallel_concurrent(pool_size):
    """
    Uses multiple processes to make requests to the search API.
    :param pool_size: number of worker processes
    """
    pass


def business_info(business_id):
    """
    Makes a request to Yelp's business API and retrieves the business data in JSON format.
    Dumps the JSON response into mongodb.

    Creates a separate MongoClient instance for each thread.

    :param business_id:
    """
    client = MongoClient()
    db = client[DB_NAME]
    coll = db[COLLECTION_NAME]

    business_path = BUSINESS_PATH + business_id
    response = request(API_HOST, business_path, BEARER_TOKEN)
    coll.insert(response)


def city_search(location):
    """
    Makes a request to Yelp's search API given the city name.
    :param city:
    :return: JSON meta data for top 20 businesses.
    """
    url_params = {
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, BEARER_TOKEN, url_params=url_params)


def scrape_sequential():
    """
    Scrapes the business's meta data for a list of cities
    and for each business scrapes the content.
    """
    coll.remove({})  # Remove previous entries from collection in Mongodb.
    with open('../data/cities') as f:
        cities = f.read().splitlines()
        for city in cities:
            response = city_search(city)
            business_ids = [business['id'] for business in response['businesses']]
            for business_id in business_ids:
                business_info(business_id)


if __name__ == '__main__':
    t = Timer(lambda: scrape_sequential())
    print("Completed sequential in %s seconds." % t.timeit(1))

    t2 = Timer(lambda: scrape_parallel_concurrent(POOL_SIZE))
    print("Completed parallel in %s seconds." % t2.timeit(1))
