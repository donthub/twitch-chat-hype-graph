import re

from easygui import enterbox


class Util:

    def get_id(self):
        url = enterbox("Enter Twitch VOD URL or ID:")
        pattern = re.compile(r'^.*?(\d+).*?$')
        return pattern.match(url).group(1)
