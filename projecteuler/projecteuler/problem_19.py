"""Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import datetime

def countingSundays(first_year: int, last_year: int) -> int:
    """Return the number of times the first day of the month is a Sunday between two years inclusive.

    Args:
        first_year(int): Start year of time period (inclusive)
        last_year(int): End year of time period (inclusive)

    Returns:
        int: Number of times the first day of the month is a Sunday
    """
    year_range = range(first_year, last_year+1)
    month_range = range(1,13)

    sunday_cnt = sum(1 for month in month_range for year in year_range if datetime(year, month, 1).weekday() == 6)

    return sunday_cnt
