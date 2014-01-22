import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import NumericProperty, ListProperty, \
        ObjectProperty, ReferenceListProperty
from kivy.graphics import Color, Ellipse, Rectangle, Triangle
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

# define again in kv file, search and fix it
tile_size = 28.0

class Hero(Widget):
    '''
    The role controlled by the player
    '''
    speed = NumericProperty(4)

class Ghost(Widget):
    '''
    The enemy
    '''
    speed = NumericProperty(4)
    # color must set default as a list of 3 elements!
    color = ListProperty([0, 0, 0])

    def __init__(self, **kwargs):
        super(Ghost, self).__init__(**kwargs)

class StartWidget(Widget):
    '''
    Put pictures, graphs, reactive in the keyboard input
    '''
    hero = ObjectProperty()
    gred = ObjectProperty()
    gpink = ObjectProperty()
    gblue = ObjectProperty()
    goran = ObjectProperty()
    characters = ReferenceListProperty(gred, gpink, hero, gblue, goran)

    def __init__(self, **kwargs):
        super(StartWidget, self).__init__(**kwargs)

        # import window after config.set takes effect
        from kivy.core.window import Window
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if text == ' ':
            # start the game
            print 'before start, remove current schedule'
            Clock.unschedule(sm.current_screen.widget.update)
            print "start the game"
            sm.current = "play"
            Clock.schedule_interval(sm.current_screen.widget.update, 1)
        return True

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
        # when __init__ called, the width/height is still default
        # value, which is (100, 100), so let's add tile w/h here
        self.tile_w = int(math.floor(self.width / tile_size))
        self.tile_h = int(math.floor(self.height/ tile_size))
        superdots = ((0, 0), (0, self.tile_h - 1), (self.tile_w - 1, 0), \
                (self.tile_w - 1, self.tile_h - 1))
        for x in range(self.tile_w):
            for y in (0, self.tile_h - 1):
                self.draw_one_dot(x, y, (x, y) in superdots)
        for y in range(self.tile_h):
            for x in (0, self.tile_w - 1):
                self.draw_one_dot(x, y, (x, y) in superdots)

    def draw_arrow(self):
        with self.canvas:
            Color(0.4, 0.4, 0.4)
            Triangle(points=(580, 350, 560, 360, 560, 340))

    def update(self, dt=0):
        print 'update border & arrow'
        self.draw_border()
        self.draw_arrow()

class PlayWidget(Widget):
    '''
    Draw map, roles, scores etc.
    '''
    def update(self, dt=0):
        print 'update play screen'

class StartScreen(Screen):
    widget = ObjectProperty()

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        # the layout size is (1, 1)
        # print self.width, self.height

class PlayScreen(Screen):
    widget = ObjectProperty()

class PacManApp(App):

    def build(self):
        sm.add_widget(StartScreen(name="start"))
        sm.add_widget(PlayScreen(name="play"))

        Clock.schedule_interval(sm.current_screen.widget.update, 3)
        return sm

if __name__ == '__main__':
    from kivy.config import Config
    Config.set('graphics', 'height', 720)
    Config.set('graphics', 'width', 1280)
    sm = ScreenManager(transition=WipeTransition())
    PacManApp().run()
