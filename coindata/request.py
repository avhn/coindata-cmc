import csv
from datetime import datetime
import os
from bs4 import BeautifulSoup
import requests

TICKER_ENDPOINT = 'https://api.coinmarketcap.com/v1/ticker/'
GLOBAL_ENDPOINT = 'https://api.coinmarketcap.com/v1/global/'

# CoinMarketCap parameters
PARAMETERS = {
    'start': '20000101',
    'end': datetime.now().strftime('%Y%m%d')
}

# Time formats
CMC_TIME_FORMAT = "%b %d, %Y"
ISO8601 = "%Y-%m-%d"


def normalize(_input):
    """Returns string input as it's correspondent type."""

    if '-' in _input:
        pass
    elif '.' in _input:
        _input = float(_input)
    else:
        _input = int(_input)

    return _input


def get_global_data():
    """Global data request with json."""

    return requests.get(GLOBAL_ENDPOINT).json()


def get_ticker(limit=None):

    """
    Returns all active cryptos from CoinMarketCap.

    Args:
        limit: Optional variable for limiting request size

    Returns:
        A sequence contains all tickers. Representation:
        [ {ticker}, {ticker}, {ticker}, ... ]
    """

    if not limit:
        # get active cryptos to request all cryptos
        global_data = get_global_data()
        limit = int(global_data['active_assets']) + int(global_data['active_currencies'])

    # request
    parameters = {'limit': limit}
    ticker = requests.get(TICKER_ENDPOINT, params=parameters).json()

    return ticker


def get_id(string):
    """Find real id or verify it by looking at ticker."""

    lookup_keys = (
        'name',
        'symbol',
        'id'
    )

    result = None
    ticker = get_ticker()
    for crypto in ticker:

        for key in lookup_keys:
            if crypto[key].lower() == string.lower():
                result = crypto['id']

        if result:
            break
    return result


def retrieve_raw(crypto):

    """
    Request and parse coinmarketcap historical data.
    Html parser for tr tag.

    Args:
        crypto: Symbol, name or coinmarketcap id.

    Returns:
        A linear sequence of raw data. Representation:
        [(Date, *, *, *, ...), (Date, *, *, *, ...), ...]
    """

    _id = get_id(crypto)
    url = 'https://coinmarketcap.com/currencies/' + _id.lower() + '/historical-data/'
    response = requests.get(url, params=PARAMETERS)
    response = str(response.content)
    page = BeautifulSoup(response, 'html.parser').find_all("tr")

    data = list()
    for i, tag in enumerate(page):
        tag = tag.get_text().replace('\\n', ' ').split()
        if i == 0:
            # start line
            tag = tag[:-2] + [' '.join(tag[-2:])]
        else:
            # arrange date and numbers
            # change time format to ISO 8601
            try:
                date = datetime.strptime(' '.join(tag[0:3]), CMC_TIME_FORMAT).strftime(ISO8601)
            except ValueError:
                # end of data at tr tags
                break

            tag = [date] + [number.replace(',', '') for number in tag[3:]]

        data.append(tag)

    return data


def retrieve(crypto):

    """
    Returns CoinMarketCap history.
    Normalizes retrieve_raw's output.

    Args:
        crypto: Symbol, name or coinmarketcap id.

    Returns:
        A sequence of data. Representation:
        [ {data}, {data}, {data}, ... ]
    """

    try:
        request = retrieve_raw(crypto)

    except ConnectionError:
        print('No internet connection!')
        return None
    except BaseException as error:
        print('Invalid input, error:', error)
        return None

    keys, data = request[0], request[1:]
    result = list()
    for one_day in data:
        item = dict()
        for i, key in enumerate(keys):
            item[key] = normalize(one_day[i])
        result.append(item)

    return result


def write(crypto, dir_path=None):

    """
    Writes a csv file of the crypto to the directory.
    Uses crypto as file name, completes with '.csv'.
    If dir_path is not specified, uses os.getcwd().
    Dates represented with ISO 8601.

    Args:
        crypto: Symbol, name or coinmarketcap id, case insensitive.
        dir_path: Optional variable, directory to write file.
            If no variable passed, uses cwd.

    Returns:
        Path of written file.
    """

    if not dir_path:
        dir_path = os.getcwd()

    file_name = crypto + '.csv'
    file_path = os.path.join(dir_path, file_name)
    data = retrieve_raw(crypto)

    with open(file_path, 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    return file_path


def read(file_path):

    """
    Reads csv files written by coindata.

    Args:
        file_path: Path to read.

    Returns:
        Same output as retrieve.
    """
    result = list()

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        keys = list()

        for i, row in enumerate(reader):
            if i == 0:
                keys = row
                continue

            data = dict()
            for j, item in enumerate(row):
                data[keys[j]] = normalize(item)

            # dismiss those [] that csv.reader generates after each element
            if data:
                result.append(data)

    return result
