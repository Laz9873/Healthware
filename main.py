from kivy.lang import Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = (360, 600)


KV = '''

MDFloatLayout:
    MDSwitch:
        pos_hint: {'center_x': .40, 'center_y': .15}

    MDRaisedButton:
        text: "Today's Workout"
        md_bg_color: "red"
        pos_hint: {'center_x': .5,  'center_y': .35}
        


'''


class Healthware(MDApp):
    def build(self):
        
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "900"
        self.theme_cls.theme_style = "Dark"
        
        return Builder.load_string(KV)


Healthware().run()