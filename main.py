from kivy.lang import Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
from kivy.core.window import Window


Window.size = (360, 600)


KV = '''

#:import Snackbar kivymd.uix.snackbar.Snackbar


MDFloatLayout:


    MDCard:
        size_hint: 1.7, .1
        focus_behavior: False
        pos_hint: {"center_x": .5, "center_y": .05}
        md_bg_color: "white"
        unfocus_color: "darkgrey"
        elevation: 6

    MDLabel:
    
        font_style:  'H1'
        font_size: 20
        pos_hint: {"center_x": .54, "center_y": .15}
        text: "minigames"
        allow_selection: True
    

    MDLabel:
    
        font_name:  'HussarBold-7mRE.otf'
        font_size: 45
        pos_hint: {"center_x": .6, "center_y": .80}
        text: "Hey"
        allow_selection: True
        padding: "4dp", "4dp"
    
    MDLabel:
        font_name:  'HussarBold-7mRE.otf'
        font_size: 45
        pos_hint: {"center_x": .6, "center_y": .70}
        text: "There."
        allow_selection: True
        padding: "4dp", "4dp"


    MDSwitch:
        active: True
        pos_hint: {'center_x': .90, 'center_y': .15}
        icon_active: "check"
        
        track_color_active: "#777a9b"
        thumb_color_active: "#777a9b"
       
        on_active: Snackbar(text="Toggle minigames ON/OFF").open()


    MDRaisedButton:

        font_style:  'Subtitle1'
        text: "Today's Workout"
        md_bg_color: "#777a9b"
        pos_hint: {'center_x': .5,  'center_y': .35}


    
'''


class Healthware(MDApp):
    
    
    def build(self):
      
        screen = Builder.load_string(KV)

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        self.theme_cls.theme_style = "Dark"
        
        return screen


Healthware().run()