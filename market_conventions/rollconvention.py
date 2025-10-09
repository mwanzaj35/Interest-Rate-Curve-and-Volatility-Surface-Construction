import datetime
import date_utils


class RollConvention:
    """
    Roll convention for date adjustments in financial contexts.

    Attributes:
        name (str): The name of the roll convention.
        description (str): A brief description of the roll convention.
    """

    def adjustDay(date: datetime.date) -> datetime.date:
            """
            Adjusts the given date according to the 30/360 US convention rules.

            Args:
                date: The date to be adjusted.

            Returns: The adjusted date.
            """
            raise NotImplementedError("Subclasses should implement this method.")


class Following(RollConvention):
    """
    Following roll convention: Move to the next business day if the date falls on a weekend or holiday.
    """

    def adjustDay(date: datetime.date, holidays: set) -> datetime.date:
        """
        Adjusts the given date to the next business day if it falls on a weekend or holiday.

        Args:
            date: The date to be adjusted.
            holidays: A set of holiday dates.

        Returns: The adjusted date.
        """
        while not date_utils.is_business_day(date, holidays):
            date += datetime.timedelta(days=1)
        return date


class ModifiedFollowing(RollConvention):
    """
    Modified Following roll convention: Move to the next business day unless it falls in the next month, 
    in which case move to the previous business day.
    """

    def adjustDay(date: datetime.date, holidays: set) -> datetime.date:
        """
        Adjusts the given date according to the Modified Following convention.

        Args:
            date: The date to be adjusted.
            holidays: A set of holiday dates.

        Returns: The adjusted date.
        """
        original_month = date.month
        while not date_utils.is_business_day(date, holidays):
            date += datetime.timedelta(days=1)
        if date.month != original_month:
            date -= datetime.timedelta(days=1)
            while not date_utils.is_business_day(date, holidays):
                date -= datetime.timedelta(days=1)
        return date


class Preceding(RollConvention):
    """
    Preceding roll convention: Move to the previous business day if the date falls on a weekend or holiday.
    """

    def adjustDay(date: datetime.date, holidays: set) -> datetime.date:
        """
        Adjusts the given date to the previous business day if it falls on a weekend or holiday.

        Args:
            date: The date to be adjusted.
            holidays: A set of holiday dates.

        Returns: The adjusted date.
        """
        while not date_utils.is_business_day(date, holidays):
            date -= datetime.timedelta(days=1)
        return date


class ModifiedPreceding(RollConvention):
    """
    Modified Preceding roll convention: Move to the previous business day unless it falls in the previous month, 
    in which case move to the next business day.
    """

    def adjustDay(date: datetime.date, holidays: set) -> datetime.date:
        """
        Adjusts the given date according to the Modified Preceding convention.

        Args:
            date: The date to be adjusted.
            holidays: A set of holiday dates.

        Returns: The adjusted date.
        """
        original_month = date.month
        while not date_utils.is_business_day(date, holidays):
            date -= datetime.timedelta(days=1)
        if date.month != original_month:
            date += datetime.timedelta(days=1)
            while not date_utils.is_business_day(date, holidays):
                date += datetime.timedelta(days=1)
        return date
