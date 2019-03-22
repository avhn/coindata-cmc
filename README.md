# Coindata
[![PyPI version](https://badge.fury.io/py/coindata.svg)](https://badge.fury.io/py/coindata)
[![Python version](https://img.shields.io/badge/Python-3.5|3.6|3.7-blue.svg)](https://github.com/Anaxilaus/coindata/blob/master/.travis.yml)
[![Build Status](https://travis-ci.org/Anaxilaus/coindata.svg?branch=master)](https://travis-ci.org/Anaxilaus/coindata)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Anaxilaus/coindata/blob/master/LICENSE)

Historical data of all cryptocurrencies.

Use it for machine learning, vector prediction or for whatever you like. Be my guest.

### Install

Install with pip or clone, both works.

```
$ git clone https://github.com/Anaxilaus/coindata
$ python coindata/setup.py install
```
or just  ```$ pip install coindata```

Setup installs requirements itself. Requirements are beautifulsoup4 and requests. 

##Usage
##### Cache with `cache`

```
>>> coindata.cache('xrp')
XRP written at $PROJECT_DIR/coindata/cache/XRP.csv
```

##### Access data through `get`

```
>>> coindata.get('RIPPLE')
[ 
  [Beginning of the time]
  .
  .
  . 
  ['Date': string,
   'Open*': float,
   'High': float,
   'Low': float,
   'Close**': float,
   'Volume': float,
   'Market Cap': float,
   # additional info below #
   'date': datetime.object,
   'circulation': decimal,
   'change': float]
   . 
   .
   .
   [Today]
]
```

***Note:*** Any form of input is legit: ```xrp = XRP = ripple = RIPPLE```

#### File structure

You can use cache files for your own.

```
source-code:
    coindata:
        cache:
            CSV files
        tickers:
            JSON files
```

##### Read documentation at code for a lot more functionality.

### Notes
- Symbol, name and case doesn't matter.

```
btc = BTC = bitcoin = BITCOIN
```

- Based on USD.

- Date notation is ISO8601 in CSV files.

```
>>> coindata.ISO8601
"%Y-%m-%d"
```

#### Give this a star this if you feel this helped you. Contributions are always welcome.
