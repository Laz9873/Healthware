from kivy.app import App, Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
import kivymd.uix.button.button
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivymd.theming import ThemeManager
from kivy.uix.image import AsyncImage


Builder.load_file("hware.kv")

class HomeScreen(Screen):
    pass

class WorkoutsScreen(Screen):
    pass

class NoweightScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass



class Healthware(MDApp):

    def __init__(self, **kwargs):
        super(Healthware, self).__init__(**kwargs)
        self.previous_screen = ""
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.theme_style = "Dark"

    def build(self):
        
        return RootWidget()

 
Healthware().run()




# to do
# start back end, connect to api, work on game ect..

# fix the size of the card view
# rework for icons on workout screen
# implement the themeing options