# Coindata
[![PyPI version](https://badge.fury.io/py/coindata.svg)/](https://badge.fury.io/py/coindata)
[![Build Status](https://travis-ci.org/anaxilaus/coindata.svg?branch=master)](https://travis-ci.org/anaxilaus/coindata)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/anaxilaus/coindata/blob/master/LICENSE)

Parse any crypto's historical data from CoinMarketCap, `write .csv files` or handle as you wish.
Do not waste time.

`Compatible with Python 2 & 3.`

### Install

Install with pip:
```
pip install coindata
```
Install remotely:
```
python setup.py install
```

### Obtain data instantly.

![](https://media.giphy.com/media/bqU3p01XL126bmEatX/giphy.gif)

### Write .csv file

![](https://thumbs.gfycat.com/QuestionableConstantGander-size_restricted.gif)

`Specify write path with file_path=None parameter.`


### Get documentation with help(* func). You can use:

```
* retrieve
* write
* read
* interval
* retrieve_raw
* get_global_data
* get_ticker
* get_id
```

### Notes
`+ Use either symbol or name of crypto. Both works.`

```
# these give same outputs
>>> coindata.retrieve('ltc')
>>> coindata.retrieve('LTC')
>>> coindata.retrieve('litecoin')
>>> coindata.retrieve('LITECOIN')
```

`+ Based on USD.`

`+ Date notation is ISO8601.`

```
>>> coindata.ISO8601
"%Y-%m-%d"
```

##### Support
Tweet, or donate anytime you feel this helped you.

[![Twitter](https://img.shields.io/twitter/url/https/github.com/anaxilaus/coindata.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20this%20out:&url=https%3A%2F%2Fgithub.com%2Fanaxilaus%2Fcoindata)
```
BTC: 16XwDdxUaphSX4yWDTTiSfNy2dTyEZ5MLy
ETH: 0x35F4B63f7eBBB2E6080F7f9f797A068004faf323
LTC: LdukNLZqzeEvvFYMw98L9Rj8AYvP86BhEe
```
