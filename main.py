from kivy.app import App, Builder
import kivymd.uix.boxlayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard 
import kivymd.uix.button.button
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivymd.theming import ThemeManager
from kivy.uix.image import AsyncImage
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.bottomsheet import MDListBottomSheet


Builder.load_file("hware.kv")

#  class A:
#         def __init__(self):
#             pass
#         def x(self):
#             print('x')

#  class B:
#         def __init__(self):
#             A().x()



class HomeScreen(Screen):
    pass

class WorkoutsScreen(Screen):
    pass

class NoweightScreen(Screen):
    
   
    # next method to allow user to cycle to the next workout
    def next(self):
        
        print(len(Healthware.noweightslist))  #print test 
        if Healthware.currentWorkout < len(Healthware.noweightslist) - 1 :
            Healthware.currentWorkout += 1
        self.ids.noweights.source = Healthware.noweightslist[Healthware.currentWorkout]
        print(Healthware.currentWorkout) #print test
    
    def back(self):

        print(len(Healthware.noweightslist))  #print test 
        if Healthware.currentWorkout != 0:
            Healthware.currentWorkout -= 1
        self.ids.noweights.source = Healthware.noweightslist[Healthware.currentWorkout]
        print(Healthware.currentWorkout) #print test

    def reset(self):
        self.ids.noweights.source = Healthware.noweightslist[0]



class RootWidget(ScreenManager):
    pass



class Healthware(MDApp):

    currentWorkout = 0
    noweightslist = ['Noweights/1428.gif','Noweights/3655.gif', 'Noweights/0001.gif', 'Noweights/1311.gif'
                     ,'Noweights/3672.gif', 'Noweights/0628.gif']


    def __init__(self, **kwargs):
        super(Healthware, self).__init__(**kwargs) 
        self.previous_screen = ""
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.theme_style = "Dark"


    def build(self):
        
        return RootWidget()
    
    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        bottom_sheet_menu.add_item()
        bottom_sheet_menu.open()

 

if __name__ == '__main__':
    Healthware().run()

# to do
# start back end, connect to api, work on game ect..

# fix the size of the card view
# rework for icons on workout screen
# implement the themeing options