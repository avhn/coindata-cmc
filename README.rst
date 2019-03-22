Coindata
========
|PyPI|
|Python|
|Build Status|
|License|

Historical data all cryptocurrencies.

Use it for machine learning, vector prediction or for whatever you like. Be my guest.

Install
-------

Install with pip or clone, both works.

.. code:: bash

    $ git clone https://github.com/Anaxilaus/coindata
    $ python coindata/setup.py install
    
or just do ``pip install coindata``

Setup installs requirements itself. Requirements are beautifulsoup4 and requests. 

Usage
-----

Cache with ``cache``
------------------------------

.. code:: python

    >>> coindata.cache('xrp')

Access data through ``get``
---------------------------

.. code:: python

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
        
``Note:`` Any form of input is legit: ``xrp = XRP = ripple = RIPPLE``

File structure:
---------------

::

    source-code:
        coindata:
            cache:
                CSV files
            tickers:
                JSON files


``Read documentation at code for a lot more functionality``

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


Give this a star if you feel this helped you. Contributions always welcome.

.. |PyPI| image:: https://badge.fury.io/py/coindata.svg
    :target: https://badge.fury.io/py/coindata
.. |Build Status| image:: https://travis-ci.org/Anaxilaus/coindata.svg?branch=master
    :target: https://travis-ci.org/Anaxilaus/coindata
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/LICENSE
.. |Python| image:: https://img.shields.io/badge/Python-3.5|3.6|3.7-blue.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/.travis.yml
