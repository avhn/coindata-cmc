"""Takes snapshot of the day, provides realpaths to other modules."""
import json
import os
import time

from . import request
from .request import ISO8601


# initialize archive folders
# uses this file's path as container directory
_TODAY = time.strftime(ISO8601)
_CONTAINER_DIR = os.path.dirname(os.path.realpath(__file__))

_SNAPSHOT_ARCHIVE_DIR = os.path.join(_CONTAINER_DIR, 'snapshots')
if not os.path.exists(_SNAPSHOT_ARCHIVE_DIR):
    os.mkdir(_SNAPSHOT_ARCHIVE_DIR)
    
_TICKER_DIR = os.path.join(_CONTAINER_DIR, 'tickers')
if not os.path.exists(_TICKER_DIR):
    os.mkdir(_TICKER_DIR)

# below for access of other modules
LATEST_TICKER_PATH = None
TICKERS = sorted(os.listdir(_TICKER_DIR))
LATEST_SNAPSHOT_DIR = None
SNAPSHOTS = sorted(os.listdir(_SNAPSHOT_ARCHIVE_DIR))
if SNAPSHOTS:
    # if there's any cached snapshot, initialize cache paths
    LATEST_SNAPSHOT_DIR = os.path.join(_SNAPSHOT_ARCHIVE_DIR, SNAPSHOTS[-1])
    LATEST_TICKER_PATH = os.path.join(_TICKER_DIR, TICKERS[-1])


def snapshot(top):

    """Takes snapshot.

        Args:
            top: Decimal, highest rank of the snapshot from ticker.
    """

    # initialize snapshot directory and ticker file path
    _SNAPSHOT_DIR = os.path.join(_SNAPSHOT_ARCHIVE_DIR, _TODAY)
    if not os.path.exists(_SNAPSHOT_DIR):
        os.mkdir(_SNAPSHOT_DIR)

    _TICKER_FILEPATH = os.path.join(_TICKER_DIR, _TODAY + '.json')

    # update global variables
    global LATEST_SNAPSHOT_DIR, LATEST_TICKER_PATH
    LATEST_SNAPSHOT_DIR, LATEST_TICKER_PATH = _SNAPSHOT_DIR, _TICKER_FILEPATH

    # dump ticker
    ticker = request.get_ticker()
    with open(_TICKER_FILEPATH, 'w') as file:
        file.write(json.dumps(ticker))
    # fetch symbols
    cryptos = [i['symbol'] for i in ticker[:top]]
    
    # fetch, parse and write
    for i, crypto in enumerate(cryptos):
        request.write(crypto, _SNAPSHOT_DIR)
        print(i + 1, "- {} fetched".format(crypto))

    print('Snapshot successful. Written at', _SNAPSHOT_DIR, 'and', _TICKER_DIR)


def take(top=100):
    """Takes snapshot with exception handlers.

        Args:
            top: Decimal, highest rank of the snapshot from ticker.
    """
    try:
        snapshot(top)

    except ConnectionError:
        print('No internet connection!')

    except KeyboardInterrupt:
        print(os.linesep + 'Exiting...')
