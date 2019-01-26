Coindata
========
|PyPI|
|Python|
|Build Status|
|License|

Take one snapshot, use all data as cached.

Use it for machine learning, vector prediction or for whatever you like. Be my guest.

How this works?
---------------
You take one snapshot, and access hundreds of cryptos without slowing down.

Basically, this program parses all historical data, stores/caches at CSV files through running a snapshot.
When you access through this package, requesting a data vector, calculates what coinmarketcap doesn't give you,
like circulation supply, daily percentage change, datetime object etc. and returns the vector.

If you want, you can use .csv files seperately.

File structure:
---------------

::

    source-code:
        coindata:
            snapshots:
                CSV files
            tickers:
                JSON files


Install
-------

Install with pip or clone, both works.

.. code:: bash

    $ pip install coindata
    ---- or ----
    $ git clone git@github.com:anaxilaus/coindata
    $ python coindata/setup.py install

Modules
-------

There are 3 modules you will use:

::

    snapshot
    parser
    request

Update cache with ``snapshot``
------------------------------

``Note:`` It will ask for a snapshot at initial import, and show you the progress, write out the cache path.

.. code:: python

    >>> coindata.snapshot.take()

Get data with ``parser``
------------------------

.. code:: python

    >>> coindata.parser.vector_of('btc')
        [
          . . .
         [ 'Date': string,
           'Open*': float,
           'High': float,
           'Low': float,
           'Close**': float,
           'Volume': float,
           'Market Cap': float,
           # additional info below #
           'date': datetime.object,
           'circulation': decimal,
           'change': float ]
           . . .
        ]

Get specific with ``request``
-----------------------------

You don't need to use if you don't want to get specific. API related operations. ( write, read, retrieve without writing, get ticker etc. )

``Note:`` I recommend caching with snapshot.

.. code:: python

    # write all history of one $indicator to $where as CSV file
    >>> coindata.request.write($indicator, $where)


Get documentation for more with built-in help() or read the code.

Important Notes
---------------

``+ Symbol, name and case doesn't matter.``

::

    btc = BTC = bitcoin = BITCOIN

``+ Based on USD.``

``+ Date notation is ISO8601 in CSV files.``
.. code:: python

    >>> coindata.ISO8601
    "%Y-%m-%d"


Give this a star this if you feel this helped you.

Also, if you want to buy a beer:

::

    BTC: 16XwDdxUaphSX4yWDTTiSfNy2dTyEZ5MLy
    ETH: 0x35F4B63f7eBBB2E6080F7f9f797A068004faf323
    LTC: LdukNLZqzeEvvFYMw98L9Rj8AYvP86BhEe


.. |PyPI| image:: https://badge.fury.io/py/coindata.svg
    :target: https://badge.fury.io/py/coindata
.. |Build Status| image:: https://travis-ci.org/Anaxilaus/coindata.svg?branch=master
    :target: https://travis-ci.org/Anaxilaus/coindata
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/LICENSE
.. |Python| image:: https://img.shields.io/badge/Python-3.5|3.6|3.7-blue.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/.travis.yml
