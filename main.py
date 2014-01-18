import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, \
        ObjectProperty, ReferenceListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.config import Config
from kivy.clock import Clock

# define again in kv file, search and fix it
tile_size = 28.0

class Hero(Widget):
    speed = NumericProperty(4)

class Ghost(Widget):
    speed = NumericProperty(4)
    # color must set default as a list of 3 elements!
    color = ListProperty([0, 0, 0])

    def __init__(self, **kwargs):
        super(Ghost, self).__init__(**kwargs)

class StartScreen(Widget):
    hero = ObjectProperty()
    gred = ObjectProperty()
    gpink = ObjectProperty()
    gblue = ObjectProperty()
    goran = ObjectProperty()
    characters = ReferenceListProperty(gred, gpink, hero, gblue, goran)

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    def draw_one_dot(self, left, bottom, is_super):
        dot_size = 4
        if is_super:
            dot_size = 12
        offset = (tile_size - dot_size) * 3 / 4
        x = left * tile_size + offset
        y = bottom * tile_size + offset
        with self.canvas:
            Color(1, 0.86, 0.5)
            Ellipse(pos = (x, y), size = (dot_size, dot_size))

    def draw_border(self):
        tw = int(math.floor(self.width / tile_size))
        th = int(math.floor(self.height/ tile_size))
        superdots = ((0, 0), (0, th - 1), (tw - 1, 0), (tw - 1, th - 1))
        for x in range(tw):
            for y in (0, th - 1):
                self.draw_one_dot(x, y, (x, y) in superdots)
        for y in range(th):
            for x in (0, tw - 1):
                self.draw_one_dot(x, y, (x, y) in superdots)

#    def update(self, dt):
#        self.draw_border()

class PlayScreen(Widget):
    pass

class PacManApp(App):

    def build(self):
        ss = StartScreen()
        ss.draw_border()
        #Clock.schedule_interval(ss.update, 1 / 60.0)
        return ss

if __name__ == '__main__':
    Config.set('graphics', 'height', 720)
    Config.set('graphics', 'width', 1280)
    PacManApp().run()
