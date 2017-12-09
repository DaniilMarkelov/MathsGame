import kivy
import random
import time
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from functools import partial
from kivy.properties import ObjectProperty
from kivy.clock import Clock

layout = FloatLayout(size=(300, 300)) 

class TestApp(App):
    current_app = ObjectProperty(None)

    def build(self):
        self.current_app = TestApp()
        layout.clear_widgets()

        no1 = random.randint(1, 10)
        no2 = random.randint(1, 10)
        answer = no1 + no2   

        Sum = str(no1) + "+" + str(no2) + "="
        label = Label(text= Sum,
                      pos= (5, 40),
                      font_size='100sp')
        layout.add_widget(label)

        random_button = random.randint(1, 3)

        button_1 = Button(text= str(answer + random.randint(1, 5)),
                          size_hint= [.33, .3],
                          pos= (0, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer = False))
        layout.add_widget(button_1)
    
        button_2 = Button(text= str(answer - random.randint(1, 5)),
                          size_hint= [.33, .3],
                          pos= (267.5, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer =False))
        layout.add_widget(button_2)
        
        button_3 = Button(text= str(answer),
                          size_hint= [.33, .3],
                          pos= (535, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer = True))
        layout.add_widget(button_3)

        return layout

    def correction(self, event, answer):
        if self.current_app:
            self.current_app.stop()
        if answer==True:
            self.current_app = Correct()
        else:
            self.current_app = Wrong()
        self.current_app.run()

class Correct(App):
    def build(self):
        self.current_app = TestApp()
        layout.clear_widgets()
        Clock.schedule_once(self.loop, 1)
        correct = Label(text= 'Correct!',
                        pos= (5, 20),
                        font_size='200sp')
        layout.add_widget(correct)
        return layout

    def loop(self, dt):
        layout.clear_widgets()
        self.current_app.run()
 
class Wrong(App):
    def build(self):
        self.current_app = TestApp()
        layout.clear_widgets()
        Clock.schedule_once(self.loop, 1)
        wrong = Label(text= 'Wrong!',
                      pos= (5, 20),
                      font_size='200sp')
        layout.add_widget(wrong)
        return layout

    def loop(self, dt):
        layout.clear_widgets()
        self.current_app.run()


app = TestApp()
app.run()
