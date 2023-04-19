from dependencies import *


Builder.load_file("hware.kv")


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
    

    def build(self):
        
        return RootWidget()
    
    def toggle_theme(self):
        
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
        
    

    def show_example_grid_bottom_sheet(self):

        bottom_sheet_menu = MDGridBottomSheet()
        bottom_sheet_menu.add_widget(
            MDLabel(text="Label 2", halign="center", valign="middle")
            )
        bottom_sheet_menu.open()
    

if __name__ == '__main__':
    Healthware().run()

# to do
# start back end, connect to api, work on game ect..

# fix the size of the card view
# rework for icons on workout screen
# implement the themeing options