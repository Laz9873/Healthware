from dependencies import *

# import child classes
from child_classes import *


# Parent classes 
class RootWidget(ScreenManager):
    pass


class Healthware(MDApp):
    
    currentWorkout = 0
    noweightslist = ['Noweights/1428.gif','Noweights/3655.gif', 'Noweights/0001.gif', 'Noweights/1311.gif'
                     ,'Noweights/3672.gif', 'Noweights/0628.gif']
    
    noweights_name = ["Wrist circles",
                       "Walking high knees lunge",
                       "Situps","Wide hand push up",
                       "Back and forth step",
                       "Monster walk"]

    noweightsdescription = ["Wrist circles"" \ntarget muscle: Forearms",
                            "Walking high knees lunge"" \ntarget muscle: cardiovascular system",
                            "Situps"" \ntarget muscle: abs", 
                            "Wide hand push up"" \ntarget muscle: pectorals",
                            "Back and forth step"" \ntarget muscle: cardiovascular system",
                            "Monster walk"" \ntarget muscle: glutes"]

    def __init__(self, **kwargs):
        super(Healthware, self).__init__(**kwargs) 
        self.previous_screen = ""

    
    def build(self):
        Builder.load_file("hware.kv")
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        return RootWidget()
    
    def next(self):
        if Healthware.currentWorkout < 5:
            Healthware.currentWorkout += 1

    def back(self):
        if Healthware.currentWorkout != 0:
            Healthware.currentWorkout -= 1
    
    def reset(self):
        Healthware.currentWorkout = 0

    def show_Modal(self):
        view = ModalView(size_hint=(.5, .5))
        view.add_widget(MDLabel(text=Healthware.noweightsdescription[Healthware.currentWorkout],halign= 'center'))
        view.open()



obj = Healthware()

if __name__ == '__main__':
    Healthware().run()

# to do
# start back end, connect to api, work on game ect..
# rework for icons on workout screen
# implement the themeing options
# resize gifs, modal view
# add padding to ! icon
# add workout tip under each workout
# connect minigames with progress bar and switch