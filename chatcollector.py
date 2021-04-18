import json
import os

import twitch

from settings import Settings
from util import Util


class ChatCollector:

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self, id):
        if os.path.exists(f'chatlogs/{id}.json'):
            return

        print('Downloading VOD chat logs. Please stand by ...')
        helix = twitch.Helix(self.settings.client_id, self.settings.client_secret)
        video = helix.video(id)

        duration = Util.parse_duration(video.duration)

        comments = []
        for comment in video.comments:
            print(f'Reading comment: {round(comment.content_offset_seconds)}/{duration}')
            comments.append({"content_offset_seconds": comment.content_offset_seconds})

        content = {
            "video": {
                "duration": video.duration
            },
            "comments": comments
        }

        with open(f'chatlogs/{id}.json', 'w') as file:
            json.dump(content, file)
