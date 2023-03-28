from kivy.app import App, Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
import kivymd.uix.button.button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemeManager


Builder.load_file("hware.kv")

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
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.theme_style = "Dark"

    def build(self):
        
        return RootWidget()

 
Healthware().run()




# to do
# fix the size of the card view
# implement the themeing options