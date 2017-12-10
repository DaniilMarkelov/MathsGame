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
current_app = ObjectProperty(None) 
random_button = 0

class TestApp(App):
   
    def build(self):
        global random_button
        current_app = TestApp()

        no1 = random.randint(1, 10)
        no2 = random.randint(1, 10)
        answer = no1 + no2   

        Sum = str(no1) + "+" + str(no2) + "="
        label = Label(text= Sum,
                      pos= (5, 40),
                      font_size='100sp')
        layout.add_widget(label)

        random_button = random.randint(1, 3)

        if random_button == 1:
            answer_1 = answer 
            answer_2 = answer + random.randint(1, 5)
            answer_3 = answer - random.randint(1, 5)

        if random_button == 2:
            answer_1 = answer - random.randint(1, 5)
            answer_2 = answer
            answer_3 = answer + random.randint(1, 5)

        if random_button == 3:
            answer_1 = answer + random.randint(1, 5)
            answer_2 = answer - random.randint(1, 5)
            answer_3 = answer

        button_1 = Button(text= str(answer_1),
                          size_hint= [.33, .3],
                          pos= (0, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no = 1))
        layout.add_widget(button_1)
    
        button_2 = Button(text= str(answer_2),
                          size_hint= [.33, .3],
                          pos= (267.5, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no = 2))
        layout.add_widget(button_2)
        
        button_3 = Button(text= str(answer_3),
                          size_hint= [.33, .3],
                          pos= (535, 0),
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no = 3))
        layout.add_widget(button_3)

        return layout

    def correction(self, event, answer_no):
        if answer_no == random_button:
            current_app = Correct()
        else:
            current_app = Wrong()
        current_app.run()

class Correct(App):
    def build(self):
        global current_app
        current_app = TestApp()
        layout.clear_widgets()
        Clock.schedule_once(self.loop, 1)
        correct = Label(text= 'Correct!',
                        pos= (5, 20),
                        font_size='200sp')
        layout.add_widget(correct)
        return layout

    def loop(self, dt):
        layout.clear_widgets()
        current_app.run()
 
class Wrong(App):
    def build(self):
        global current_app
        current_app = TestApp()
        layout.clear_widgets()
        Clock.schedule_once(self.loop, 1)
        wrong = Label(text= 'Wrong!',
                      pos= (5, 20),
                      font_size='200sp')
        layout.add_widget(wrong)
        return layout

    def loop(self, dt):
        layout.clear_widgets()
        current_app.run()

if __name__ == "__main__":
    app = TestApp()
    app.run()
