## Coindata
[![PyPI version](https://badge.fury.io/py/coindata.svg)](https://pypi.org/project/coindata/)
[![Build Status](https://travis-ci.org/Anaxilaus/coindata.svg?branch=master)](https://travis-ci.org/Anaxilaus/coindata)
[![Python Version](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-blue.svg)](./.travis.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

Historical data of all cryptos from CoinMarketCap.

**Examples:**

- CSV
    - [`BTC.csv`](./examples/cache_files/BTC.csv)
    - [`XRP.csv`](./examples/cache_files/XRP.csv)
    - [`ETH.csv`](./examples/cache_files/ETH.csv)

- JSON
    - [`BTC.json`](./examples/dump_json/btc.json)
    - [`XRP.json`](./examples/dump_json/xrp.json)
    - [`ETH.json`](./examples/dump_json/eth.json)


## Install

**Pip:**

```
$ pip install coindata
```

**Clone repository:**

```
$ git clone https://github.com/Anaxilaus/coindata
$ python coindata/setup.py install
```

`Requirements:` beautifulsoup4 and requests. Setup installs requirements itself. 

## Usage
#### Cache and get

```
>>> coindata.cache('xrp')
XRP written at $PROJECT_DIR/coindata/cache/XRP.csv
>>> coindata.get('xrp')
[
  {Beginning of the time}
  .
  .
  . 
  {'Date': string,
   'Open*': float,
   'High': float,
   'Low': float,
   'Close**': float,
   'Volume': float,
   'Market Cap': float,
   
   # additional calculated info below #
   'circulation': decimal,
   'change': float,
   'date': datetime.object
   }
   . 
   .
   .
   {Today}
]
```

#### Dump as JSON to use elsewhere.

[`Example JSON dump.`](./examples/dump_json)


## File structure

You can use cache files:

```
source-code
├── coindata
│   ├── cache
│   │   ├── CSV files
│   ├── tickers
│   │   ├── JSON files
```

[`Example cache files.`](./examples/cache_files)

**Read documentation at code for a lot more functionality.**

## Notes

- Symbol, name and case-insensitive.

```
btc = BTC = bitcoin = BITCOIN
```

- Based on USD.

- Date notation is ISO8601 in CSV files.

```
>>> coindata.ISO8601
"%Y-%m-%d"
```

### Give this a star if you feel this helped you. Contributions are always welcome.
