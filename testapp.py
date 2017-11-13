import kivy
import random
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class TestApp(App):
	def build(self):
				
		layout = FloatLayout(size=(300, 300))
		
		no1 = random.randint(1, 10)
		no2 = random.randint(1, 10)
		answer = no1 + no2

		Sum = str(no1) + "+" + str(no2) + "="
		label = Label(text= Sum,
					  pos= (5, 40),
					  font_size='100sp')
		layout.add_widget(label)

		def correct(instance):
			layout.clear_widgets()
			correct = Label(text= 'Correct!',
						  pos= (5, 20),
						  font_size='200sp')
			layout.add_widget(correct)
			return layout

		def wrong(instance):
			layout.clear_widgets()
			wrong = Label(text= 'Wrong!',
						  pos= (5, 20),
						  font_size='200sp')
			layout.add_widget(wrong)
			return layout

		random_button = random.randint(1, 3)

		if random_button == 1:

			b1 = Button(text= str(answer),
				  	    size_hint= [.33, .3],
				  	    pos= (0, 0),
						font_size='75sp',
						on_press= correct)
			layout.add_widget(b1)
		
			b2 = Button(text= str(answer + random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (267.5, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b2)
			
			b3 = Button(text= str(answer - random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (535, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b3)
			return layout

		if random_button == 2:

			b1 = Button(text= str(answer - random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (0, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b1)
		
			b2 = Button(text= str(answer),
				  	    size_hint= [.33, .3],
				  	    pos= (267.5, 0),
						font_size='75sp',
						on_press= correct)
			layout.add_widget(b2)
			
			b3 = Button(text= str(answer + random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (535, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b3)
			return layout

		if random_button == 3:

			b1 = Button(text= str(answer + random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (0, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b1)
		
			b2 = Button(text= str(answer - random.randint(1, 5)),
				  	    size_hint= [.33, .3],
				  	    pos= (267.5, 0),
						font_size='75sp',
						on_press= wrong)
			layout.add_widget(b2)
			
			b3 = Button(text= str(answer),
				  	    size_hint= [.33, .3],
				  	    pos= (535, 0),
						font_size='75sp',
						on_press= correct)
			layout.add_widget(b3)
			return layout


TestApp().run()
