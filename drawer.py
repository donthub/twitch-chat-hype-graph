import webbrowser

import matplotlib.pyplot as plt
import matplotlib.ticker
import mplcursors as mplcursors
from matplotlib.backend_bases import MouseButton

from settings import Settings
from util import Util


class Drawer:

    def __init__(self, settings: Settings, content):
        self.settings = settings
        self.content = content
        self.id = content['video']['id']
        self.duration = content['video']['duration']
        self.created_at = content['video']['created_at']
        self.cursor = None

    def draw(self, data_x, data_y):
        fig, ax = plt.subplots()
        ax.plot(data_x, data_y)

        ax.set_xlabel('Time')
        ax.set_ylabel('Comments')
        ax.set_title(self.get_title())

        formatter = matplotlib.ticker.FuncFormatter(lambda s, x: Util.seconds_to_time_colon(s))
        ax.xaxis.set_major_formatter(formatter)

        self.cursor = mplcursors.cursor(hover=True)

        plt.connect('button_press_event', self.on_click)
        plt.connect('close_event', self.on_close)
        plt.show()

    def get_title(self):
        title = self.content['video']['title']
        length = Util.seconds_to_time_colon(Util.time_letter_to_seconds(self.duration))
        created_at = self.content['video']['created_at']
        return f'{title} - {length} - {created_at}'

    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            selection = self.cursor.selections[0].target[0]
            seconds = max(0, selection - self.settings.preview)
            time = Util.seconds_to_time_letter(seconds)
            webbrowser.open(f'https://twitch.tv/videos/{self.id}?t={time}')

    def on_close(self, event):
        exit(-1)
