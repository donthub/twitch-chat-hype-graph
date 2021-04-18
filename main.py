from chatcollector import ChatCollector
from datatransformer import DataTransformer
from drawer import Drawer
from settings import Settings
from util import Util

if __name__ == '__main__':
    settings = Settings()
    id = Util.get_id()

    content = ChatCollector(settings).collect(id)

    data_x, data_y = DataTransformer(settings).transform(content)
    Drawer(settings, content).draw(data_x, data_y)

    while True:
        pass
