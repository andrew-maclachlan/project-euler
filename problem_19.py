# Problem 19
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-19-counting-sundays 

from datetime import datetime

def countingSundays(first_year, last_year) -> int:
    """
    Return the number of times the first day of the month is a Sunday between to years inclusive.
    """
    year_range = range(first_year, last_year+1)
    month_range = range(1,13)

    sunday_cnt = sum([1 for month in month_range for year in year_range if datetime(year, month, 1).weekday() == 6])

    return sunday_cnt
