from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, \
        ObjectProperty
from kivy.graphics import Color
from kivy.config import Config

class Hero(Widget):
    speed = NumericProperty(4)

class Ghost(Widget):
    speed = NumericProperty(4)
    # color must set default as a list of 3 elements!
    color = ListProperty([0, 0, 0])

    def __init__(self, **kwargs):
        super(Ghost, self).__init__(**kwargs)

class StartScreen(Widget):
    gred = ObjectProperty()

class PlayScreen(Widget):
    pass

class PacManApp(App):

    def build(self):
        ss = StartScreen()
        print ss.gred.center
        return StartScreen()

if __name__ == '__main__':
    Config.set('graphics', 'height', 720)
    Config.set('graphics', 'width', 1280)
    PacManApp().run()
