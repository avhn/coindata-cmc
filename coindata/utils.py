"""Utility functions defined here."""
import csv
from datetime import datetime
import json

from .request import ISO8601


def to_datetime(string):
    """Convert string to datetime object.

    Args:
        string: ISO8601 formatted string

    Returns:
        Correspondent datetime object.
    """

    return datetime.strptime(string, ISO8601)


def format_date(date, reformat='%b %d, %Y'):

    """Format date.

    Args:
        date: ISO8601 formatted string or datetime object
        reformat: New format representation. Default is "%b %d, %Y"

    Returns:
        String formatted with reformat arg.
    """

    if isinstance(date, str):
        date = to_datetime(date)

    return date.strftime(reformat)


def write_csv(path, iterable):
    """Write iterable to path as csv."""
    if not path.endswith('.csv'):
        path += '.csv'

    with open(path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(iterable)


def dump_json(data, filepath):
    """Dump data as JSON."""

    try:
        with open(filepath, 'w') as file:
            json.dump(data, filepath)
    except TypeError as e:
        print("Data isn't JSON compatible.\n", e)
