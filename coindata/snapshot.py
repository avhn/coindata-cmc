import json
import os
import time
import coindata


# initilize archive folders
# uses this file's path as in project directory
_today = time.strftime(coindata.ISO8601)
_project_dir = os.path.dirname(os.path.realpath(__file__))

snapshot_archive_dir = os.path.join(_project_dir, 'snapshots')
os.path.exists(snapshot_archive_dir) or os.mkdir(snapshot_archive_dir)

snapshot_dir = os.path.join(snapshot_archive_dir, _today)
os.path.exists(snapshot_dir) or os.mkdir(snapshot_dir)

ticker_dir = os.path.join(_project_dir, 'tickers')
os.path.exists(ticker_dir) or os.mkdir(ticker_dir)


def snapshot(top=150):

    """Takes snapshot.

    Args:
        top: Decimal, highest rank of the snapshot from ticker.
    """

    ticker = coindata.get_ticker()
    
    # dump ticker
    with open(os.path.join(ticker_dir, _today + '.json'), 'w') as file:
        file.write(json.dumps(ticker))

    # fetch symbols
    cryptos = [i['symbol'] for i in ticker[:top]]

    portfolio = read_portfolio()
    for c in portfolio:
        if c.upper() not in cryptos:
            cryptos.append(c)

    # write
    for i, c in enumerate(cryptos):
        coindata.write(c, snapshot_dir)
        print(i + 1, "- {} fetched".format(c))
        
    print('Successfully written at', snapshot_dir, 'and', ticker_dir)


def main():
    try:
        snapshot()

    except ConnectionError:
        print('No internet connection!')


if __name__ == '__main__':
    main()
