import math
import re

from easygui import enterbox


class Util:

    @staticmethod
    def get_id():
        url = enterbox("Enter Twitch VOD URL or ID:")
        pattern = re.compile(r'^.*?(\d+).*?$')
        return pattern.match(url).group(1)

    @staticmethod
    def time_letter_to_seconds(time) -> int:
        seconds = 0

        hours_pattern = re.compile(r'(\d+)h.*')
        hours_match = hours_pattern.match(time)
        if hours_match:
            seconds += int(hours_match.group(1)) * 3600

        minutes_pattern = re.compile(r'.*?(\d+)m.*')
        minutes_match = minutes_pattern.match(time)
        if minutes_match:
            seconds += int(minutes_match.group(1)) * 60

        seconds_pattern = re.compile(r'.*?(\d+)s')
        seconds_match = seconds_pattern.match(time)
        if seconds_match:
            seconds += int(seconds_match.group(1))

        return seconds

    @staticmethod
    def seconds_to_time(seconds: int, h_separator, m_separator, s_separator) -> str:
        time = str(math.floor(seconds / 3600)) + h_separator
        time += Util.prefix_number(math.floor(seconds % 3600 / 60)) + m_separator
        time += Util.prefix_number(math.floor(seconds % 60)) + s_separator
        return time

    @staticmethod
    def seconds_to_time_letter(seconds: int) -> str:
        return Util.seconds_to_time(seconds, h_separator='h', m_separator='m', s_separator='s')

    @staticmethod
    def seconds_to_time_colon(seconds):
        return Util.seconds_to_time(seconds, h_separator=':', m_separator=':', s_separator='')

    @staticmethod
    def prefix_number(number: int) -> str:
        str_number = str(number)
        if len(str_number) == 1:
            str_number = '0' + str_number
        return str_number
