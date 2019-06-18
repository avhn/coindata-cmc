#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import coindata


def main(indicator):
    """Cache and print get."""

    coindata.cache(indicator)
    print(coindata.get(indicator))


if __name__ == '__main__':
    indicator = input("Type symbol or name: ")
    main(indicator)
