import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty # type: ignore
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import hashlib

# ============= CUPON =============
def generar_hash(codigo):
    hash_obj = hashlib.sha256(codigo.encode())
    return hash_obj.hexdigest()[:7]
# =================================


class MainScreen(Screen):
    pass

class SecondScreen(Screen):

    def consultar_ticket(self, trackeo_codigo):
        trackeo_codigo = trackeo_codigo.strip()
        try:
            # Enviar una solicitud GET a la API `/tickets`
            response = requests.get("http://localhost:5001/ticket")
            
            if response.status_code == 200:
                tickets = response.json()  # Convertir la respuesta en una lista de diccionarios
                
                # Buscar un ticket que coincida con el id_trackeo ingresado
                #match = next((ticket for ticket in tickets if ticket['id_trackeo'] == trackeo_codigo), None)
                
                match = False

                for tiket in tickets:
                    print(tiket['id_trackeo'], "==", trackeo_codigo)
                    print(type(tiket['id_trackeo']))
                    print(type(trackeo_codigo))
                    if tiket['id_trackeo'] == trackeo_codigo:
                        match = True

                if match:
                    print(f"Match encontrado: {match}")
                    
                    # Pasar el ID de trackeo a la pantalla `track_view`
                    track_screen = self.manager.get_screen('track_view')
                    track_screen.id_trackeo = trackeo_codigo
                    
                    # Cambiar a la pantalla `track_view`
                    self.manager.current = 'track_view'
                else:
                    # Mostrar mensaje si no se encuentra el código
                    self.dialog = MDDialog(title="Estado trackeo",text=f"Tu código: {trackeo_codigo}, caduco o no existe",size_hint=(0.8, 0.3))
                    self.dialog.open()
            else:
                print(f"Error en la API: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error en la conexión: {e}")

class TrackScreen(Screen):
    id_trackeo = StringProperty("")  # Esta propiedad debe ser pasada desde la otra pantalla.
     # Inicializamos con el primer estado como "truck-delivery".

    def on_enter(self):
        # Inicia la consulta cada 3 segundos para consultar el estado del ticket
        Clock.schedule_interval(self.consultar_estado_ticket, 3)

    def on_leave(self):
        # Detener la consulta cuando se salga de la pantalla
        Clock.unschedule(self.consultar_estado_ticket)

    def consultar_estado_ticket(self, dt):

        try:
            # Hacer la consulta al endpoint `/ticket` para obtener la lista de tickets
            response = requests.get(f"http://localhost:5001/ticket/{self.id_trackeo}")  # Asegúrate de que la URL esté correcta.
            
            if response.status_code == 200:
                tickets = response.json()  # Convertir la respuesta a una lista de diccionarios
                
                # Buscar el ticket correspondiente al id_trackeo
                estado = tickets.get("estado","") #match = next((ticket for ticket in tickets if ticket['id_trackeo'] == int(self.id_trackeo)), None)
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

    def on_enter(self):  # Se ejecuta al entrar en esta vista
        self.obtener_cupones()

    def obtener_cupones(self):
        try:
            response = requests.get("http://localhost:5001/qr")  # Llamada al endpoint
            if response.status_code == 200:
                self.promo_data = response.json()  # Guardar los datos en la lista
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
