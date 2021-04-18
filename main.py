import os

from chatcollector import ChatCollector
from datatransformer import DataTransformer
from drawer import Drawer
from settings import Settings
from util import Util

if __name__ == '__main__':
    settings = Settings()
    id = Util().get_id()

    if not os.path.exists(f'chatlogs/{id}.json'):
        ChatCollector(settings).collect(id)

    data_x, data_y = DataTransformer(settings).transform(id)
    Drawer(settings, id).draw(data_x, data_y)

    while True:
        pass
