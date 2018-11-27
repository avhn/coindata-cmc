import json
import os
from .main import read as read_data
from .snapshot import snapshot_archive_dir, ticker_dir


# initilize latest archive paths
SNAPSHOTS = snapshot_archive_dir
TICKERS = ticker_dir

try:
    # snapshot directory
    LATEST_FOLDER = sorted(os.listdir(SNAPSHOTS))[-1]
    SNAPSHOT = os.path.join(SNAPSHOTS, LATEST_FOLDER)

    # ticker file
    LATEST_FILE = sorted(os.listdir(TICKERS))[-1]
    TICKER = os.path.join(TICKERS, LATEST_FILE)

except FileNotFoundError as e:
    print('Invalid filepath!', os.linesep, e)


def symbols():
    """Returns all symbols from latest snapshot."""

    result = list()

    for s in os.listdir(SNAPSHOT):

        # remove .csv from names
        s = s[:-4]
        result.append(s)

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
    """Get ticker of a specific crypto from latest snapshot.

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
        with open(TICKER) as file:
            ticker = json.loads(file.read())

    except FileNotFoundError:
        raise FileNotFoundError('Ticker file is not at: ', TICKER)

    # normalize numbers from str
    for i in range(len(ticker)):
        for key in ticker[i]:
            ticker[i][key] = normalize_str(ticker[i][key])


    if indicator:
        keys = ['symbol', 'name', 'id']

        for data in ticker:
            for key in keys:
                if type(data[key]) is str and data[key].upper() == indicator.upper():
                    return data

        # indicator is not fould in snapshot
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
    filepath = os.path.join(SNAPSHOT, filename)

    return read_data(filepath)
