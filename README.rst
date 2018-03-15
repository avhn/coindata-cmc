Coindata
========
|PyPI|
|Build Status|
|License|

Parse any crypto's historical data from CoinMarketCap, write .csv files or handle as you wish. Do not waste time.

Compatible with Python 2 & 3.

Install
-------

Install with pip:

.. code:: bash

   pip install coindata

Install remotely:

.. code:: bash

   python setup.py install

Usage
-----

Retrieve
^^^^^^^^

Obtain data instantly?:

.. code:: python

   >>> import coindata
   >>> coindata.retrieve('LTC')

Done!

.. code:: python

   [

   {'Date': '2018-07-07', 'Open*': 83.40, 'High': 86.20, 'Low': 80.70, 'Close**': 86.20, 'Volume': 238937000, 'Market Cap': 4778260000},
   .
   .
   .
   {'Date': '2013-04-28', 'Open*': 4.30, 'High': 4.40, 'Low': 4.18, 'Close**': 4.35, 'Volume': '-', 'Market Cap': 73773400}

   ]

Write .csv file
^^^^^^^^^^^^^^^

.. code:: python

   coindata.write('LTC', 'FILE_PATH.csv')

+------------+--------+-------+-------+----------+-----------+------------+
| Date       | Open*  | High  | Low   | Close**  | Volume    | Market Cap |
+============+========+=======+=======+==========+===========+============+
| 2018-07-07 | 83.40  | 86.20 | 80.70 | 86.20    | 238937000 | 4778260000 |
+------------+--------+-------+-------+----------+-----------+------------+
| 2018-07-06 | 83.84  | 84.60 | 81.32 | 83.38    | 253160000 | 4801850000 |
+------------+--------+-------+-------+----------+-----------+------------+
| ...        | ...    | ...   | ...   | ...      | ...       | ...        |
+------------+--------+-------+-------+----------+-----------+------------+
| ...        | ...    | ...   | ...   | ...      | ...       | ...        |
+------------+--------+-------+-------+----------+-----------+------------+

Get documentation with help(* func). You can use:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   * retrieve
   * write
   * read
   * interval
   * retrieve_raw
   * get_global_data
   * get_ticker
   * get_id

Notes
^^^^^
``+ Use either symbol or name of crypto. Both works.``

.. code:: python

   # these give same outputs
   >>> coindata.retrieve('ltc')
   >>> coindata.retrieve('LTC')
   >>> coindata.retrieve('litecoin')
   >>> coindata.retrieve('LITECOIN')

``+ Based on USD.``

``+ Date notation is ISO8601.``

.. code:: python

   >>> coindata.ISO8601
   "%Y-%m-%d"

Support
^^^^^^^
Tweet, or donate anytime you feel this helped you.

|Tweet|

- BTC: 16XwDdxUaphSX4yWDTTiSfNy2dTyEZ5MLy
- ETH: 0x35F4B63f7eBBB2E6080F7f9f797A068004faf323
- LTC: LdukNLZqzeEvvFYMw98L9Rj8AYvP86BhEe



.. |PyPI| image:: https://badge.fury.io/py/coindata.svg
    :target: https://badge.fury.io/py/coindata
.. |Build Status| image:: https://travis-ci.org/anaxilaus/coindata.svg?branch=master
    :target: https://travis-ci.org/anaxilaus/coindata
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/anaxilaus/coindata/blob/master/LICENSE
.. |Tweet| image:: https://img.shields.io/twitter/url/https/github.com/anaxilaus/coindata.svg?style=social
    :target: https://twitter.com/intent/tweet?text=Check%20this%20out:&url=https%3A%2F%2Fgithub.com%2Fanaxilaus%2Fcoindata
