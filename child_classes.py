from main import obj, Screen, Widget, Rectangle, Window, Clock, Healthware, App, MDRectangleFlatButton

from kivymd.uix.snackbar import Snackbar

def collides(rect1, rect2):
        r1x = rect1[0][0]
        r1y = rect1[0][1]
        r2x = rect2[0][0]
        r2y = rect2[0][1]
        r1w = rect1[1][0]
        r1h = rect1[1][1]
        r2w = rect2[1][0]
        r2h = rect2[1][1]

        if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False
        

# child classes
class HomeScreen(Screen):
    pass
        

class WorkoutsScreen(Screen):
    pass


class NoweightScreen(Screen, Widget):
    
    
    def resetnoweights(self):
        obj.reset()
        self.ids.noweights.source = obj.noweightslist[0]
        self.ids.noweightslabeltext.text = obj.noweights_name[0]
        if self.ids.progress.value > 60:
            self.finish()
        self.ids.progress.value = 0

        
        
    def nextnoweights(self):
        obj.next()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]
        if self.ids.progress.value !=100:
            self.ids.progress.value += 20
        if self.ids.progress.value > 60:
            self.halfway()
        if self.ids.progress.value == 100:
            btn = MDRectangleFlatButton(text='Play Game!', 
                                        pos_hint={"center_x": 0.5, "center_y": 0.30})
            
            btn.bind(on_press=self.clkfunc)
            self.add_widget(btn)
            
    def clkfunc(self , obj):
        App.get_running_app().stop()
    
    def backnoweights(self):
        obj.back()
        self.ids.noweights.source = obj.noweightslist[obj.currentWorkout]
        self.ids.noweightslabeltext.text = obj.noweights_name[obj.currentWorkout]
        if self.ids.progress.value !=0:
            self.ids.progress.value -= 20


    def gameScreen(self):
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self) 
        self._keyboard.bind(on_key_down= self._on_key_down)
        self._keyboard.bind(on_key_up= self._on_key_up)


        if self.ids.progress.value == 60:
            with self.canvas:
                self.player= Rectangle(source="sonic.gif",pos=(self.width-100,0), size_hint=(100,100))
                self.enemy = Rectangle(source="finish.png",pos=(0,0), size=(80,80))

            self.keysPressed = set()

            Clock.schedule_interval(self.move_step,0)
        


    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up= self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)


    def _on_key_up(self, keyboard, keycode):    
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    # set dt in function call
    def move_step(self, dt):
        

        currentx = self.player.pos[0]
        currenty = self.player.pos[1]
    
        step_size = 100 * dt

        if "a" in self.keysPressed:
            currentx -= step_size
        if "d" in self.keysPressed:
            currentx += step_size 

        self.player.pos = (currentx, currenty)

        if collides((self.player.pos,self.size), (self.enemy.pos, self.enemy.size)):
            self.finish()
            
    

    def finish(self):
        self.canvas.remove(self.player)
        self.canvas.remove(self.enemy)


    def halfway(self):
        Snackbar(
        text="Your almost There!",
        snackbar_x="50dp",
        snackbar_y="50dp",
        size_hint_x=.5
        ).open()