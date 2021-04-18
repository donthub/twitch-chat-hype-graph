import json

from settings import Settings
from util import Util


class DataTransformer:

    def __init__(self, settings: Settings):
        self.settings = settings

    def transform(self, id):
        with open(f'chatlogs/{id}.json', 'r') as file:
            content = json.load(file)

        duration = Util.parse_duration(content['video']['duration'])
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
