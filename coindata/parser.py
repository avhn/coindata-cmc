import json
import os

from .request import read as read_data
from .cache import CACHE_DIR, LATEST_TICKER_PATH
from .utils import to_datetime


def symbols():
    """Returns all symbols from latest snapshot."""

    result = list()

    for symbol in os.listdir(CACHE_DIR):
        # remove .csv from names
        symbol = symbol[:-4]
        result.append(symbol)

    return result


def normalize_str(string):
    """String to number."""

    try:
        if string.isdigit():
            result = int(string)
        else:
            result = round(float(string), 3)

        return result

    except (ValueError, AttributeError):
        return string


def parse_ticker(indicator=None):

    """
    Get ticker of a specific crypto from latest snapshot.
    If no argument passed, returns whole ticker.

    Args:
        indicator: indicator of crypto

    Returns:
        A sequence of dicts.
        If indicator passed, returns just one dict.
    Raises:
        ValueError: Indicator not found
        FileNotFoundError: Path is wrong
    """

    # read ticker
    try:
        with open(LATEST_TICKER_PATH) as file:
            ticker = json.loads(file.read())

    except BaseException as e:
        raise ValueError("Can't parse ticker, error: ", e)


    # normalize numbers from str
    for i in range(len(ticker)):
        for key in ticker[i]:
            ticker[i][key] = normalize_str(ticker[i][key])


    if indicator:
        keys = ['symbol', 'name', 'id']

        for data in ticker:
            for key in keys:
                if isinstance(data[key], str) and data[key].upper() == indicator.upper():
                    return data

        # indicator is not found in snapshot
        raise ValueError('Indicator not found: ', indicator)

    else:
        return ticker


def parse(indicator):
    """Parse data from latest snapshot in project dir.

    Args:
        indicator: Indicator of crypto

    Returns:
        Sequence of dicts.
        Reads with coindata.read, therefore output is
        represented by it.
    """

    # normalize if needed
    if indicator.endswith('.csv'):
        indicator = indicator[:4]

    # confirm or find real symbol
    symbol = parse_ticker(indicator)['symbol']

    # set path of data
    filename = symbol.upper() + '.csv'
    filepath = os.path.join(CACHE_DIR, filename)

    return read_data(filepath)


def vector_of(indicator):
    """Fetch daily data.

    Computes daily change, circulation supply, datetime object
    from cached snapshot. Using both ticker and historical data.

    Args:
        indicator: Indicator of crypto

    Returns:
        Old to new sequence.
        Full list of keys for one item:

        dict_keys([
            'Date': string,
            'Open*': float,
            'High': float,
            'Low': float,
            'Close**': float,
            'Volume': float,
            'Market Cap': float,

            # additional info below #
            'date': datetime.object,
            'circulation': decimal,
            'change': float,
        ])

        Computation of additional keys:

            'date': datetime.datetime object
            'circulation': Market Cap / Open*
            'change': Market Cap / previous Market Cap
    """

    result = list()
    max_supply = parse_ticker(indicator)['max_supply']
    previous = None

    for data in parse(indicator):
        if data['Market Cap'] != '-':

            # generate datetime object
            date = to_datetime(data['Date'])
            data['date'] = date

            if previous:

                # add daily change
                data['change'] = round(data['Market Cap'] / previous['Market Cap'], 3)

                # add circulation
                circulation = int(data['Market Cap'] / data['Open*'])
                if max_supply and max_supply < circulation:
                    circulation = max_supply

                data['circulation'] = circulation

                # set new previous
                result.insert(0, data)

            previous = data

    return result
