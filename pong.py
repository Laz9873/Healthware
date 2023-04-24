from datetime import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.label import Label


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            ball.velocity = speedup * (offset - ball.velocity)


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos





class PongGame(Widget):
    ball = ObjectProperty(None)

    def victory(self, win):
        if win:
            self.win_label = Label(size_hint = (None, None),
                               text = 'Winner!',
                               markup = True,
                               font_size = 70,
                               color = [1,0,0,1]
                               )
        else:
            self.win_label = Label(size_hint=(None, None),
                               text='Loser!',
                               markup=True,
                               font_size=70,
                               color=[1, 0, 0, 1]
                               )

        self.win_label.center = self.center
        self.win_label.bind(on_ref_press=self.click_win_label)
        self.win_label.texture_update()
        self.add_widget(self.win_label)



    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        top = 1
        win = True

        if (self.player2.center_y > self.height) or (top == 1):
            self.player2.center_y -= 5

        if self.player1.score == 5:
            self.victory(win)

        if self.player2.score == 5:
            win = False
            self.victory(win)


        if self.player2.center_y < 0:
            self.player2.center_y = self.height

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        if (self.ball.x < self.x) and (self.player2.score != 5):
            self.player2.score += 1
            self.serve_ball()

        if (self.ball.right > self.width) and (self.player1.score != 5):
            self.player1.score += 1
            self.serve_ball()

    def click_win_label(self, instance, value):
        self.remove_widget(self.win_label)
        self.initialize()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
            print(self.player1.center_y)




class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

