import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from kivy.clock import mainthread
import hashlib
import json

class SecondScreen(Screen):

    nombre_cliente = ""
    direccion_cliente = ""

    def obtener_datos_cliente(self, id_trackeo):
        try:
            response = requests.get(f"http://localhost:5001/tickets/{id_trackeo}")
            
            if response.status_code == 200:
                datos = response.json()
                
                if 'Payload' in datos:
                    payload = json.loads(datos['Payload'])
                    detalles_envio = json.loads(payload['detallesEnvio'])

                    self.nombre_cliente = f"{detalles_envio['nombre']} {detalles_envio['apellido']}"
                    self.direccion_cliente = detalles_envio['direccion']

                    self.ids.nombre_label.text = f"Pedido para: {self.nombre_cliente}"
                    self.ids.direccion_label.text = f"Dirección: {self.direccion_cliente}"
                    print(f"Datos del cliente obtenidos con éxito.")
                    print(f"Nombre: {self.nombre_cliente}")
                    print(f"Dirección: {self.direccion_cliente}")
                else:
                    print("Error: 'Payload' no encontrado en la respuesta.")
            else:
                print(f"Error {response.status_code}, no se pudo obtener los datos del cliente.")
        except requests.RequestException as e:
            print(f"Error al obtener datos del cliente: {e}")

    @mainthread
    def enviar_estado(self, estado):
        id_trackeo = id_trackeo = self.ids.input_trackeo.text.strip()
        if not id_trackeo:
            self.mostrar_error("Por favor ingresa un ID de rastreo válido.")
            return

        url = "http://localhost:5001/ticket"
        payload = {
            "ID_TRACKEO": id_trackeo,
            "Estado": estado
        }
        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                self.mostrar_exito("Estado actualizado con éxito.")
            else:
                self.mostrar_error(f"Error al actualizar el estado: {response.json().get('mensaje', 'Desconocido')}")
        except requests.RequestException as e:
            self.mostrar_error(f"No se pudo conectar con el servidor: {str(e)}")

    def mostrar_exito(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(mensaje)

    def consultar_ticket(self, estado):
        self.enviar_estado(estado)

class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '600'
        
        Builder.load_file('designDelivery.kv')  

        self.sm = ScreenManager()
        
        self.sm.add_widget(SecondScreen(name='second_view'))

        return self.sm


if __name__ == '__main__': 
    MyApp().run()
