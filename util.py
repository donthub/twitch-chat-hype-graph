import re

from easygui import enterbox


class Util:

    def get_id(self):
        url = enterbox()
        pattern = re.compile(r'^.*?(\d+).*?$')
        return pattern.match(url).group(1)
