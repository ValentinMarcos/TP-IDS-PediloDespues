import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty # type: ignore
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
    def enviar_ID(self, instance):
        trackeo_codigo= instance.text
        print(f'Código de rastreo ingresado: {trackeo_codigo}')
    pass

class TrackScreen(Screen):
    pass

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
        id_cliente = "cliente12"
        nombre_promo = "foodpedilodespues"
        codigo = f"{id_cliente}_{nombre_promo}"
        hash_generado = self.promo_data[index]['hash']

        self.dialog = MDDialog(
            title="Código de Promoción",
            text=f"Tu código de descuento es: {hash_generado}",
            size_hint=(0.8, 0.3)
        )
        self.dialog.open()
    
class MyApp(MDApp):

    current_step = 0
    state_icons = ListProperty(["truck-delivery", "", "", "", ""])  # Asi empieza, luego se actualiza dependiendo el estado del pedido

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

        Clock.schedule_interval(self.simular_estado, 5)


        return self.sm

    def simular_estado(self, dt):
        if self.current_step < 5: 
            self.estado_pedido(self.current_step)
            self.current_step += 1

    def estado_pedido(self, current_step):

        steps = ["Autorizando", "Armando pedido", "En camino", "En su domicilio", "Pedido Entregado"]
        self.state_icons = [
            "check" if i < current_step else "truck-delivery" if i == current_step else ""
            for i in range(len(steps))
        ]


    def cambiar_vista(self):
        self.sm.current = "second_view"


if __name__ == '__main__': 
    MyApp().run()
