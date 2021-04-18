import math
import webbrowser

import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

from settings import Settings


class Drawer:

    def __init__(self, settings: Settings, id):
        self.settings = settings
        self.id = id

    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            time = max(0, event.xdata - self.settings.preview)
            str_time = str(math.floor(time / 3600)) + 'h'
            str_time += str(math.floor(time % 3600 / 60)) + 'm'
            str_time += str(math.floor(time % 60)) + 's'
            webbrowser.open(f'https://twitch.tv/videos/{self.id}?t={str_time}')

    def on_close(self, event):
        exit(-1)

    def draw(self, data_x, data_y):
        fig, ax = plt.subplots()
        ax.plot(data_x, data_y)
        plt.connect('button_press_event', self.on_click)
        plt.connect('close_event', self.on_close)
        plt.show()
