import sys

import tcd

from settings import Settings


class ChatCollector:

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect(self, id):
        print('Downloading VOD chat logs. Please stand by ...')

        sys.argv = []
        sys.argv.append('--video')
        sys.argv.append('--client-id')
        sys.argv.append(self.settings.client_id)
        sys.argv.append('--client-secret')
        sys.argv.append(self.settings.client_secret)
        sys.argv.append('-v')
        sys.argv.append(id)
        sys.argv.append('--format')
        sys.argv.append('json')
        sys.argv.append('--output')
        sys.argv.append('chatlogs')
        tcd.main()
