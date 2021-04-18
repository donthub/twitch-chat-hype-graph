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
            return self.load_existing(id)
        else:
            return self.create_new(id)

    def load_existing(self, id):
        with open(f'chatlogs/{id}.json', 'r') as file:
            return json.load(file)

    def create_new(self, id):
        print('Downloading VOD chat logs. Please stand by ...')
        helix = twitch.Helix(self.settings.client_id, self.settings.client_secret)
        video = helix.video(id)

        duration = Util.time_letter_to_seconds(video.duration)
        comments = []
        for comment in video.comments:
            print(f'Reading comment: {round(comment.content_offset_seconds)}/{duration}')
            comments.append({"content_offset_seconds": comment.content_offset_seconds})

        content = {
            "video": {
                "id": video.id,
                "title": video.title,
                "duration": video.duration,
                "created_at": video.created_at
            },
            "comments": comments
        }

        with open(f'chatlogs/{id}.json', 'w') as file:
            json.dump(content, file)

        return content
