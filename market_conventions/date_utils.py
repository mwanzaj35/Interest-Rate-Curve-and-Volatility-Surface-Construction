import datetime

def is_end_of_month(date: datetime.date) -> bool:
    """
    Check if a given date is the end of the month.
    """
    next_day = date + datetime.timedelta(days=1)
    return next_day.month != date.month

def end_of_month(date: datetime.date) -> bool:
    """
    Check if a given date is the end of the month.
    """
    if is_end_of_month(date):
        return date
    else:
        # Move to the last day of the month
        last_day = (date.replace(day=1) + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
        return last_day

def is_business_day(date: datetime.date, holidays: set) -> bool:
    """
    Check if a given date is a business day (not a weekend or holiday).
    """
    return date.weekday() < 5 and date not in holidays
