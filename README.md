## Coindata
[![PyPI version](https://badge.fury.io/py/coindata.svg)](https://badge.fury.io/py/coindata)
[![Python version](https://img.shields.io/badge/Python-3.5|3.6|3.7-blue.svg)](https://github.com/Anaxilaus/coindata/blob/master/.travis.yml)
[![Build Status](https://travis-ci.org/Anaxilaus/coindata.svg?branch=master)](https://travis-ci.org/Anaxilaus/coindata)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Anaxilaus/coindata/blob/master/LICENSE)

Historical data of all cryptos from CoinMarketCap.

### Install

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

### Usage
#### Cache with `cache`

```
>>> coindata.cache('xrp')
XRP written at $PROJECT_DIR/coindata/cache/XRP.csv
```

#### Access through `get`

**Note:** You can dump this data as JSON to use elsewhere.
```
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
   # additional info below #
   'date': datetime.object,
   'circulation': decimal,
   'change': float}
   . 
   .
   .
   {Today}
]
```

#### File structure

 You can use cache files:

```
source-code
├── coindata
│   ├── cache
│   │   ├── CSV files
│   ├── tickers
│   │   ├── JSON files
```

##### Read documentation at code for a lot more functionality.

### Notes

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

#### Give this a star if you feel this helped you. Contributions are always welcome.
