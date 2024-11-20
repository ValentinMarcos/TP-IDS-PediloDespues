from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton

class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    def enviar_ID(self, instance):
        trackeo_codigo= instance.text
        print(f'Código de rastreo ingresado: {trackeo_codigo}')

    pass
    
class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '600'
        Builder.load_file('design.kv')  

        self.sm = ScreenManager()
        
        self.sm.add_widget(MainScreen(name='main_view'))
        self.sm.add_widget(SecondScreen(name='second_view'))

        return self.sm

    def cambiar_vista(self):
        self.sm.current = "second_view"


if __name__ == '__main__': 
    MyApp().run()
