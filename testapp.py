import kivy
import random
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from functools import partial
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window

kivy.require('1.10.0')

layout = FloatLayout(size=(300, 300))
current_app = ObjectProperty(None)
random_button = 0
correct_score = 0
wrong_score = 0


class TestApp(App):

    def build(self):
        global random_button
        current_app = TestApp()

        random_sum = random.randint(1, 4)

        if random_sum == 1:
            no1 = random.randint(10, 50)
            no2 = random.randint(10, 50)
            answer = no1 + no2
            symbol = '+'

        if random_sum == 2:
            no1 = random.randint(10, 50)
            no2 = random.randint(10, 50)
            answer = no1 - no2
            symbol = '-'

        if random_sum == 3:
            no1 = random.randint(4, 12)
            no2 = random.randint(4, 12)
            answer = no1 * no2
            symbol = 'x'

        if random_sum == 4:
            no3 = random.randint(4, 12)
            no2 = random.randint(4, 12)
            no1 = no3 * no2
            answer = no1 / no2
            symbol = '/'

        Sum = str(no1) + str(symbol) + str(no2) + "="

        Window.clearcolor = (.15, .15, .15, .15)

        label = Label(text=Sum,
                      pos=(5, 40),
                      font_size='100sp')
        layout.add_widget(label)

        wrong_label = Label(text='wrong:  ' + str(wrong_score),
                            pos_hint={'x':  .34, 'y':  .43},
                            font_size='50sp')
        layout.add_widget(wrong_label)

        correct_label = Label(text='correct:  ' + str(correct_score),
                              pos_hint={'x': -.34, 'y': .43},
                              font_size='50sp')
        layout.add_widget(correct_label)

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

        button_1 = Button(text=str(answer_1),
                          size_hint=[.33, .3],
                          pos_hint={'x': .0, 'y': .0},
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no=1))
        layout.add_widget(button_1)

        button_2 = Button(text=str(answer_2),
                          size_hint=[.33, .3],
                          pos_hint={'x': .334, 'y': .0},
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no=2))
        layout.add_widget(button_2)

        button_3 = Button(text=str(answer_3),
                          size_hint=[.33, .3],
                          pos_hint={'x': .668, 'y': .0},
                          font_size='75sp',
                          on_press=partial(self.correction, answer_no=3))
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
        correct = Label(text='Correct!',
                        pos=(5, 20),
                        font_size='200sp')
        layout.add_widget(correct)
        return layout

    def loop(self, dt):
        global correct_score
        correct_score = correct_score + 1
        layout.clear_widgets()
        current_app.run()


class Wrong(App):
    def build(self):
        global current_app
        current_app = TestApp()
        layout.clear_widgets()
        Clock.schedule_once(self.loop, 1)
        wrong = Label(text='Wrong!',
                      pos=(5, 20),
                      font_size='200sp')
        layout.add_widget(wrong)
        return layout

    def loop(self, dt):
        global wrong_score
        wrong_score = wrong_score + 1
        layout.clear_widgets()
        current_app.run()

if __name__ == "__main__":
    app = TestApp()
    app.run()
