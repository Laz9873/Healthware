from kivy.app import App, Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
from kivy.core.window import Window
import kivymd.uix.button.button
from kivy.uix.screenmanager import Screen, ScreenManager


Window.size = (360, 600)

Builder.load_file("healthware.kv")

class HomeScreen(Screen):
    pass

class WorkoutsScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class Healthware(MDApp):

    def __init__(self, **kwargs):
        super(Healthware, self).__init__(**kwargs)
        self.previous_screen = ""

    def build(self):
        
        return RootWidget()



Healthware().run()