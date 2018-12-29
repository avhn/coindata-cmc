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

_SNAPSHOT_DIR = os.path.join(_SNAPSHOT_ARCHIVE_DIR, _TODAY)
if not os.path.exists(_SNAPSHOT_DIR):
    os.mkdir(_SNAPSHOT_DIR)
    
_TICKER_DIR = os.path.join(_CONTAINER_DIR, 'tickers')
if not os.path.exists(_TICKER_DIR):
    os.mkdir(_TICKER_DIR)

# below for access of other modules
TICKER_PATH = None
TICKERS = sorted(os.listdir(_TICKER_DIR))
LATEST_SNAPSHOT_DIR = None
SNAPSHOTS = sorted(os.listdir(_SNAPSHOT_ARCHIVE_DIR))
if SNAPSHOTS:
    LATEST_SNAPSHOT_DIR = os.path.join(_SNAPSHOT_ARCHIVE_DIR, SNAPSHOTS[-1])
    TICKER_PATH = os.path.join(_TICKER_DIR, TICKERS[-1])


def snapshot(top=150):

    """Takes snapshot.

    Args:
        top: Decimal, highest rank of the snapshot from ticker.
    """
    
    ticker = request.get_ticker()
    
    # dump ticker
    with open(os.path.join(_TICKER_DIR, _TODAY + '.json'), 'w') as file:
        file.write(json.dumps(ticker))

    # fetch symbols
    cryptos = [i['symbol'] for i in ticker[:top]]
    
    # write
    for i, crypto in enumerate(cryptos):
        request.write(crypto, _SNAPSHOT_DIR)
        print(i + 1, "- {} fetched".format(crypto))
        
    print('Successfully written at', _SNAPSHOT_DIR, 'and', _TICKER_DIR)


def main():
    try:
        snapshot()

    except ConnectionError:
        print('No internet connection!')

    except KeyboardInterrupt:
        print(os.newline + 'Exiting...')


if __name__ == '__main__':
    main()
