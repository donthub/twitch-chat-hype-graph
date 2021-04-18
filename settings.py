import json
import os
import shutil


class Settings:

    def __init__(self):
        if not os.path.exists('settings.json'):
            shutil.copyfile('settings.json.reference', 'settings.json')

        with open('settings.json', 'r') as file:
            settings = json.load(file)

        self.client_id = settings['client_id']
        self.client_secret = settings['client_secret']
        if self.is_empty(self.client_id) or self.is_empty(self.client_secret):
            print(
                'Please fill "client_id" and "client_secret" in settings.json. Can be acquired by registering application at https://dev.twitch.tv/console/apps/')
            exit(-1)

        self.interval = settings['interval']
        self.neighbor = settings['neighbor']
        self.preview = settings['preview']

    def is_empty(self, input):
        return input is None or len(input) == 0
