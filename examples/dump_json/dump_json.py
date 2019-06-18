#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import coindata


def main(indicator):
    """Write indicator as indicator.json"""

    coindata.cache(indicator)
    data = coindata.get(indicator)
    coindata.utils.dump_json(data, indicator + '.json')


if __name__ == '__main__':
    indicator = input('Type symbol or name: ')
    main(indicator)
