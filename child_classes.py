from main import obj, Screen


# child classes
class HomeScreen(Screen):
    pass
        

class WorkoutsScreen(Screen):
    pass


class NoweightScreen(Screen):
    
    
    def resetnoweights(self):
        obj.reset()
        self.ids.noweights.source = obj.noweightslist[0]
        self.ids.noweightslabeltext.text = obj.noweights_name[0]
        
        
    def nextnoweights(self):
        obj.next()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]

    
    def backnoweights(self):
        obj.back()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]

