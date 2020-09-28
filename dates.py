# -*- coding: utf-8; -*-
'''A selection of functions to handle dates.'''

import calendar
from datetime import date, timedelta

__author__ = "Pedro Inácio"
__copyright__ = "Copyright 2015"
__version__ = "1.0"
__maintainer__ = "Pedro Inácio"
__email__ = "pedromiragaia@gmail.com"
__status__ = "Development"


def parse_date_range(dstr):
    """
    This function parses a date range with the format:
        YYYY[MM[DD]][:YYYY[MM[DD]]]
    and returns a tuple with the initial and final dates.

    Possible '-'' and '/'' characters on the input string are stripped.
    """

    # Remove - and / and split into lower and upper date bounds
    date_range = dstr.replace('-', '').replace('/', '').split(':')

    # Check length
    if len(date_range) == 0 or len(date_range) >= 3:
        raise ValueError("Incorrectly specified date range")

    # Parse lower bound of data range
    date_start = parse_date(date_range[0])

    # Parse optional upper bound of date range
    if len(date_range) == 1:
        date_end = parse_date(date_range[0], round_up=True)
    else:
        date_end = parse_date(date_range[1], round_up=True)

    # Check valid range
    if date_start > date_end:
        raise ValueError("Incorrect date range. Upper bound of date range " +
                         "must be later than lower bound.")

    # Return tuple
    return (date_start, date_end)


def parse_date(dstr, round_up=False):
    """
    This function recieves a string with the format YYYY[MM[DD]] and returns
    the corresponding date object.
    Missing elements are assumed to be 1, i.e., 2006 corresponds to 2006/01/01

    Optional argument round_up specifies whether to round the date up instead,
    i.e., 2006 corresponds to 2006/12/31
    """

    year = int(dstr[0:4])
    if round_up:
        month = int(dstr[4:6]) if dstr[4:6] != '' else 12
        # get last day of the month
        aux = calendar.monthrange(year, month)
        day = int(dstr[6:8]) if dstr[6:8] != '' else aux[1]
    else:
        month = int(dstr[4:6]) if dstr[4:6] != '' else 1
        day = int(dstr[6:8]) if dstr[6:8] != '' else 1

    return date(year, month, day)


def range_date(date_start, date_end, delta=timedelta(1)):
    """
    Similar to the range function, return a list of dates
    """

    list_dates = list()
    d = date_start
    while d <= date_end:
        list_dates.append(d)
        d += delta

    return list_dates