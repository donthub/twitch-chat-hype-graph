import json
import re

from settings import Settings


class DataTransformer:

    def __init__(self, settings: Settings):
        self.settings = settings

    def transform(self, id):
        with open(f'chatlogs/{id}.json', 'r') as file:
            content = json.load(file)

        duration = self.parse_duration(content)
        interval = self.settings.interval
        neighbor = self.settings.interval

        data_x = []
        data_y = []
        for i in range(0, round(duration / interval)):
            data_x.append(i * interval)
            data_y.append([])

        for comment in content['comments']:
            comment_time = comment['content_offset_seconds']
            low_index = max(0, round((comment_time - neighbor) / interval))
            high_index = min(round((comment_time + neighbor) / interval), len(data_y) - 1)
            for i in range(low_index, high_index + 1):
                data_y[i].append(comment)

        data_y = list(map(lambda items: len(items), data_y))
        return data_x, data_y

    def parse_duration(self, content) -> int:
        duration = 0
        str_duration = content['video']['duration']

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
