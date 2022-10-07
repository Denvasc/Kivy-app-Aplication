from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')

def get_weight(m):
    value1 = str(45.99 * m / 1000)
    value2 = str(1.80 * m / 1000)
    value3 = str(5.50* m / 1000)
    value4 = str(41.99 * m / 1000)
    value5 = str(3.37 * m / 1000)
    
    return {'value1': value1, 'value2': value2, 'value3': value3, 'value4': value4, 'value5': value5}

class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingr = get_weight(mass)

        self.value1.text = ingr.get('value1')
        self.value2.text = ingr.get('value2')
        self.value3.text = ingr.get('value3')
        self.value4.text = ingr.get('value4')
        self.value5.text = ingr.get('value5')
        

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
        MyApp().run()

