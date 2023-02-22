from kivy.lang import Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
from kivy.core.window import Window
import kivymd.uix.button.button
from kivy.uix.screenmanager import Screen, ScreenManager


Window.size = (360, 600)


KV = '''


<FloatButton@FloatLayout>:
    id: float_root
    size_hint: (None, None)
    text: ''
    btn_size: (20,20)
    size: (70,70)
    bg_color: (0.119, 0.122, 0.155, .6)
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {'x':.5}
    Button:
        icon: "android"
        text: float_root.text
        on_release: app.switch_theme_style()
        markup: True
        size_hint: (None,None)
        size: float_root.btn_size
        pos_hint: {'x':2, 'y': 8}
        background_normal:''
        background_color: (0,0,0,0) 
        canvas.before:
            Color:
                rgba: float_root.bg_color
            Ellipse:
                size: self.size
                pos: self.pos


ScreenManager:
    HomeScreen:
    WorkoutsScreen:


<HomeScreen>:
    
    name: 'home'
    MDCard:
        size_hint: .7, .1
        focus_behavior: False
        pos_hint: {"center_x": .5, "center_y": .1}
        md_bg_color: "white"
        unfocus_color: "white"
        elevation: 1

    MDLabel:
    
        font_style:  'H1'
        font_size: 20
        pos_hint: {"center_x": .68, "center_y": .10}
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
        pos_hint: {'center_x': .68, 'center_y': .1}
        track_color_active: "#777a9b"
        thumb_color_active: "#777a9b"


    MDFillRoundFlatButton:

        font_style:  'Subtitle1'
        text: "Today's Workout"
        md_bg_color: "#777a9b"
        pos_hint: {'center_x': .5,  'center_y': .35}
        on_press: root.manager.current = 'workouts'
        elevation: 1

    
    FloatButton:
       


<WorkoutsScreen>:


    
    name: 'workouts'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'home'
    
    MDLabel:
        text: 'Welcome!'
        halign: 'center'



    
'''


class HomeScreen(Screen):
    pass

class WorkoutsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(WorkoutsScreen(name='workouts'))

class Healthware(MDApp):
    
    def build(self):
      
        screen = Builder.load_string(KV)
        
        return screen


    def switch_theme_style(self):
       
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light" # Themes needs to be flushed out 
        )


Healthware().run()