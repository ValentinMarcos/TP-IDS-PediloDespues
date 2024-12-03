import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import hashlib

class MainScreen(Screen):
    pass

class SecondScreen(Screen):

    def consultar_ticket(self, trackeo_codigo):
        trackeo_codigo = trackeo_codigo.strip()
        try:
            response = requests.get("http://localhost:5001/ticket")
            
            if response.status_code == 200:
                tickets = response.json()

                match = False

                for tiket in tickets:
                    print(tiket['id_trackeo'], "==", trackeo_codigo)
                    print(type(tiket['id_trackeo']))
                    print(type(trackeo_codigo))
                    if tiket['id_trackeo'] == trackeo_codigo:
                        match = True

                if match:
                    print(f"Match encontrado: {match}")
                    
                    track_screen = self.manager.get_screen('track_view')
                    track_screen.id_trackeo = trackeo_codigo
                    
                    self.manager.current = 'track_view'
                else:
                    self.dialog = MDDialog(title="Estado trackeo",text=f"Tu código: {trackeo_codigo}, caduco o no existe",size_hint=(0.8, 0.3))
                    self.dialog.open()
            else:
                print(f"Error en la API: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error en la conexión: {e}")

class TrackScreen(Screen):
    id_trackeo = StringProperty("")

    def on_enter(self):
        Clock.schedule_interval(self.consultar_estado_ticket, 3)

    def on_leave(self):
        Clock.unschedule(self.consultar_estado_ticket)

    def consultar_estado_ticket(self, dt):

        try:
            response = requests.get(f"http://localhost:5001/ticket/{self.id_trackeo}/estado")
            
            if response.status_code == 200:
                tickets = response.json()
                
                estado = tickets.get("estado","")
                estados = ["Autorizando", "Armando pedido", "En camino", "Estamos en su domicilio", "Pedido Entregado"]

                if estado in estados:
                    print(estado)
                    print("si estado")

                nuevoEstado = []

                for i in range(len(estados)):
                    nuevoEstado.append("check")
                    if estado == estados[i] :
                        nuevoEstado[i]="truck-delivery"
                        break
                
                if len(nuevoEstado)<len(estados):
                    for _ in range(len(estado)-len(nuevoEstado)):
                        nuevoEstado.append("")
                
                app = MDApp.get_running_app()
                app.state_icons = nuevoEstado
            else:
                print(f"Error al obtener los tickets: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error en la conexión: {e}")

class ErrorScreen(Screen):
    pass

class PromoScreen(Screen):
    promo_data = ListProperty([])

    def on_enter(self):
        self.obtener_cupones()

    def obtener_cupones(self):
        try:
            response = requests.get("http://localhost:5001/qr")
            if response.status_code == 200:
                self.promo_data = response.json()
                print(f"Datos obtenidos: {self.promo_data}")
            else:
                print(f"Error al obtener los datos: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error en la conexión: {e}")

    def mostrar_cupon(self, index):
        hash_generado = self.promo_data[index]['hash']

        self.dialog = MDDialog(
            title="Código de Promoción",
            text=f"Tu código de descuento es: {hash_generado}",
            size_hint=(0.8, 0.3)
        )
        self.dialog.open()
    
class MyApp(MDApp):
    state_icons = ListProperty(["","","","",""]) 

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '600'
        
        Builder.load_file('design.kv')  

        self.sm = ScreenManager()
        
        self.sm.add_widget(MainScreen(name='main_view'))
        self.sm.add_widget(SecondScreen(name='second_view'))
        self.sm.add_widget(TrackScreen(name='track_view'))
        self.sm.add_widget(PromoScreen(name='promos_view'))
        self.sm.add_widget(ErrorScreen(name='error_view'))


        return self.sm


    def cambiar_vista(self):
        self.sm.current = "second_view"


if __name__ == '__main__': 
    MyApp().run()
