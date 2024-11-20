from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.screen import Screen

class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass
    
class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '600'
        Builder.load_file('design.kv')  

        sm = ScreenManager()
        
        sm.add_widget(MainScreen(name='main_view'))

        return sm


if __name__ == '__main__': 
    MyApp().run()