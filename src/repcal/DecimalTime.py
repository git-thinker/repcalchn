from datetime import datetime, date, time
from math import floor


class DecimalTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{}:{}:{}'.format(
            self.hour,
            self.minute,
            self.second
        )

    @classmethod
    def from_standard_time(cls, standard_time, adjust_to_paris_mean=True):
        """
        Takes a time object and converts to decimal.
        If adjust_to_paris_mean is true the given time will be assumed to be GMT
        and the resulting decimal time is adjusted to Paris Mean Time.

        :param standard_time: datetime.time
        :param adjust_to_paris_mean:
        :return: string
        """
        midnight = datetime.combine(date.today(), time.fromisoformat('00:00:00'))
        target = datetime.combine(date.today(), standard_time)

        standard_seconds = (target - midnight).seconds

        if adjust_to_paris_mean:
            standard_seconds += 561

        second_ratio = 100 * 100 * 10 / (60 * 60 * 24)
        decimal_seconds = floor(standard_seconds * second_ratio)

        seconds_per_hour = 100 * 100
        seconds_per_minute = 100

        hour = decimal_seconds // seconds_per_hour
        decimal_seconds -= hour * seconds_per_hour

        minute = decimal_seconds // seconds_per_minute
        decimal_seconds -= minute * seconds_per_minute

        return cls(hour, minute, decimal_seconds)
