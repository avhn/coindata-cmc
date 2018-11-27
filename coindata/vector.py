from . import parser
from .utils import *


def vector_of(indicator):
    """Fetch daily data.

    Computes daily change,
    Args:
        indicator: Indicator of crypto

    Returns:
        Old to new sequence.
        Full list of keys for one item:

        dict_keys(['Date', 'Open*', 'High', 'Low', 'Close**', 'Volume', 'Market Cap',
        'date', 'circulation', 'change'])

        Computation of additional keys:

        'date': datetime.datetime object
        'circulation': Market Cap / Open*
        'change': Market Cap / previous Market Cap
    """

    result = list()

    max_supply = parser.parse_ticker(indicator)["max_supply"]
    previous = None

    for d in parser.parse(indicator):
        if d["Market Cap"] is not '-':

            # generate datetime object
            date = to_datetime(d['Date'])
            d['date'] = date

            if previous:

                # add daily change
                d["change"] = round(d["Market Cap"] / previous["Market Cap"], 3)

                # add circulation
                circulation = int(d["Market Cap"] / d["Open*"])
                if max_supply and max_supply < circulation:
                    circulation = max_supply

                d["circulation"] = circulation

                # set new previous
                result.insert(0, d)

            previous = d

    return result
