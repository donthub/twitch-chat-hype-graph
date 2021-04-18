import re

from easygui import enterbox


class Util:

    @staticmethod
    def get_id():
        url = enterbox("Enter Twitch VOD URL or ID:")
        pattern = re.compile(r'^.*?(\d+).*?$')
        return pattern.match(url).group(1)

    @staticmethod
    def parse_duration(str_duration) -> int:
        duration = 0

        hours_pattern = re.compile(r'(\d+)h.*')
        hours_match = hours_pattern.match(str_duration)
        if hours_match:
            duration += int(hours_match.group(1)) * 3600

        minutes_pattern = re.compile(r'.*?(\d+)m.*')
        minutes_match = minutes_pattern.match(str_duration)
        if minutes_match:
            duration += int(minutes_match.group(1)) * 60

        seconds_pattern = re.compile(r'.*?(\d+)s')
        seconds_match = seconds_pattern.match(str_duration)
        if seconds_match:
            duration += int(seconds_match.group(1))

        return duration
