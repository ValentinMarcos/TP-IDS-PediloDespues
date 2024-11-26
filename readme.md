
# Facultad de Ingenieria Universidad de Buenos Aires
## Intro desarollo Software - Catedra Lanzillotta  
## Trabajo practico Integrador (Nota : )

### Integrantes del grupo

- Juan Valentín marcos 111596 
- Leonel Rodrigo Rolon 101009 
- Ivan Poggio 113002 
- Angela Alcon 111850
- Karel Leire Luna García 105816 
- Agustin Beltrame 112552 
- Jordan Ticona 111656 

### Docentes
- Bruno Lanzillotta
- Leonel Chaves (Corrector)

# Proyecto PediloDespues - Plataforma de Pedidos

- **Frontend Web**: Una página web para realizar pedidos, una vez que el cliente realiza un pedido poniendo sus datos, como va a pagar y su direccion, se genera un ticket con un id de trackeo que se guarda en la base de datos mediante la api y con ese id se puede ver el estado del pedido. 
Para guardar en el carrito los productos se uso Localstorage para guardar en la memoria del navegador los mismos e ir mostrandolos.

- **Backend**: Un servidor Flask en Python que gestiona la lógica de negocio, permite mostrar los productos al front o a la app mobile, permite generar el ticket e ir actualizando su estado para poder mostrar el rastreo del producto, ademas permite devolver los qrs para la app mobile. 
Se comunica con una base de datos MySQL.

- **App Móvil**: Una aplicación móvil construida con Kivy que permite usar qrs que se usan para tener promociones, los mismos se guardan en la base de datos por lo que se comunica con la api para traer los mismos. Ademas permite mediante una consulta a la api mostrar el estado del producto segun su ID de Trackeo que tambien se almacena en la base de datos.

## Tecnologías Utilizadas

### Frontend
- **Python** 
- **HTML** / **CSS** / **JavaScript**
- **Jinja** para el renderizado dinámico de las plantillas en el lado del servidor
- **Flask** para la creación del servidor web
- **Puerto 5000** para la ejecución del servidor frontend

### Backend
- **Python** (Flask)
- **MySQL Connector** para interactuar con la base de datos MySQL
- **Puerto 5001** para la ejecución del servidor backend

### App Móvil
- **Kivy** para la construcción de la aplicación móvil

## Instalación y Configuración
En cada carpeta del proyecto hay un archivo requirements y un innit.sh para inicializar el proyecto, usando pip install -r "requirements.txt" en cada carpeta es suficiente para poder correrlo.

En cuanto a la base de datos es necesario tener seteada la password root en "12345678" para poder conectarse exitosamente a la base de datos, una vez seteada la password se puede correr el archivo
crear_base.py y mediante una consulta a /cargardatos se llena la misma con los productos en la tabla Productos.

