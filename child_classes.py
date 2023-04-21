from main import obj, Screen

from dependencies import MDGridBottomSheet, MDLabel








# child classes





class HomeScreen(Screen):
    pass
        

class WorkoutsScreen(Screen):
    pass




class NoweightScreen(Screen):
    
    
    def resetnoweights(self):
        self.ids.noweights.source = obj.noweightslist[0]
        self.ids.noweightslabeltext.text = obj.noweights_name[0]
    
    # next method to allow user to cycle to the next workout
    def nextnoweights(self):
        
        if obj.currentWorkout < len(obj.noweightslist) - 1 :
            obj.next()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]
    # back method to allow users to cycle to previous workout
    def backnoweights(self):

        if obj.currentWorkout != 0:
            obj.back()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]
    
    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        bottom_sheet_menu.add_widget(
            MDLabel(id= 'desc', text= obj.noweightsdescription[obj.currentWorkout], halign= 'center')
            )
        bottom_sheet_menu.open()
