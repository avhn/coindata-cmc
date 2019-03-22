import json
import os
import time

from . import request
from . import parser
from .request import ISO8601


# uses this file's path as project directory
TODAY = time.strftime(ISO8601)
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

CACHE_DIR = os.path.join(PROJECT_DIR, 'cache')
TICKER_DIR = os.path.join(PROJECT_DIR, 'tickers')

# initialize archive folders
if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)
if not os.path.exists(TICKER_DIR):
    os.mkdir(TICKER_DIR)


def cache_ticker():
    """Writes ticker to cache and returns it."""

    global LATEST_TICKER_PATH

    _ticker_path = os.path.join(TICKER_DIR, TODAY + '.json')
    ticker = request.get_ticker()
    with open(_ticker_path, 'w') as file:
        file.write(json.dumps(ticker))

    LATEST_TICKER_PATH = os.path.join(PROJECT_DIR, _ticker_path)
    print('Ticker written at', LATEST_TICKER_PATH)

    return ticker


# find latest ticker's absolute path
LATEST_TICKER_PATH = None
_tickers = sorted(os.listdir(TICKER_DIR))

if len(_tickers) > 0:
    LATEST_TICKER_PATH = os.path.join(TICKER_DIR, _tickers[-1])

if not LATEST_TICKER_PATH:
    cache_ticker()


def cache(indicator):

    """Caches indicator.

    Write cache files as "{symbol_of_indicator}.csv".

        Args:
            indicator: Symbol or name of the crypto. Case insensitive.
    """

    # dump ticker
    # fetch symbols

    indicator = parser.parse_ticker(indicator)['symbol']
    request.write(indicator, CACHE_DIR)

    print(indicator, 'written at', os.path.join(CACHE_DIR, indicator + '.csv'))
