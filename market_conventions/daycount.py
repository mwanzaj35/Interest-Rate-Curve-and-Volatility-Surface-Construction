"""
References:
Jorg Kienitz (2015). Interest Rate Derivatives Explained Volume 1: Products and Markets (10th Edition). Pearson.

This module implements day count conventions as described in the book.
"""

import datetime
from enum import Enum

class DayCountConvention(Enum):
    ACTUAL_360 = "Actual/360"
    ACTUAL_365 = "Actual/365"
    ACTUAL_ACTUAL = "Actual/Actual"
    THIRTY_360 = "30/360"
    THIRTY_360_US = "30/360 US"
    THIRTY_360_EU = "30/360 European"

class DayCount:
    """
    Base class for day count conventions.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        """
        Calculate the year fraction between two dates.
        This method should be overridden by subclasses to implement specific day count conventions.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def __repr__(self):
        return f"{self.__class__.__name__}()"
    

class Actual360(DayCount):
    """
    Actual/360 day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        time_delta = (end_date - start_date).days
        return time_delta / 360.0
    
class Actual365(DayCount):
    """
    Actual/365 Fixed day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        time_delta = (end_date - start_date).days
        return time_delta / 365.0
    
class ActualActual(DayCount):
    """
    Actual/Actual day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        time_delta = (end_date - start_date).days
        # Calculate the number of days in the year of the start date
        year_length = 366 if (start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0)) else 365
        return time_delta / year_length
    
class Thirty360(DayCount):
    """
    30/360 day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        d1 = min(start_date.day, 30)
        d2 = min(end_date.day, 30)
        m1 = start_date.month
        m2 = end_date.month
        y1 = start_date.year
        y2 = end_date.year

        return ((360 * (y2 - y1)) + (30 * (m2 - m1)) + (d2 - d1)) / 360.0
    
class Thirty360US(DayCount):
    """
    30/360 US day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        d1 = start_date.day
        d2 = end_date.day
        m1 = start_date.month
        m2 = end_date.month
        y1 = start_date.year
        y2 = end_date.year

        if d1 == 31:
            d1 = 30
        if d2 == 31 and d1 == 30:
            d2 = 30

        return ((360 * (y2 - y1)) + (30 * (m2 - m1)) + (d2 - d1)) / 360.0
    
class Thirty360EU(DayCount):
    """
    30/360 European day count convention.
    """

    def year_fraction(start_date: datetime.date, end_date: datetime.date) -> float:
        d1 = min(start_date.day, 30)
        d2 = min(end_date.day, 30)
        m1 = start_date.month
        m2 = end_date.month
        y1 = start_date.year
        y2 = end_date.year

        if d1 == 31:
            d1 = 30
        if d2 == 31:
            d2 = 30

        return ((360 * (y2 - y1)) + (30 * (m2 - m1)) + (d2 - d1)) / 360.0
    