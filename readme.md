
# Facultad de Ingenieria Universidad de Buenos Aires
## Intro desarollo Software - Catedra Lanzillotta  
## Trabajo practico Integrador (Nota : 10 )

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

# Objetivo

El objetivo de este trabajo era crear un aplicativo web en el que podamos ofrecerle a alguna franquicia de comida una aplicación de entregas en la que ellos puedan cargar los productos que tengan en venta y que sus clientes puedan elegir lo que desean pedir y ademas les ofrecemos un servicio de seguimiento de su pedido en vivo, también ofrecemos una app para el delivery que actualiza en tiempo real el estado del pedido.
 Se crea una base de datos con las tablas de productos, de tickets y de qr, los qr funcionarian como promo para usar presencial en el local. Los tickets tienen un identificador unico y un codigo de trackeo el cual puede ser usado tanto en pc como en movil.
Tanto la pagina web como el aplicativo movil son adaptables al dispositivo en el que este el usuario.

# Introducción

Lo que nos diferencia de otras aplicaciones de delivery es la facilidad con la que el cliente puede ordenar su menú, permitiendole hacer su pedido sin ningún registro. Tras ingresar sus datos y confirmarlos, recibe un ID único de trackeo con el cual puede haer el seguimiento tanto en el sitio web como en la app mobile, este mismo persiste en la base de datos.

# Conclusión 

Al principio consideramos la elevada dificultad que llevaria realizar el TP en relación al traslado de información, y aun asi, tomamos la decisión de seguirlo por la motivacion y dedicacion del equipo, animado por la resolucion inicial que le habiamos dado, siendo este un boceto del funcionamiento. A lo largo del TP nos organizamos y repartimos las tareas mediante Trello, documentamos los endpoints de la API con Swagger y nos comunicamos mediante Discord.

Una de las principales problematicas fue el despliegue de la aplicacion en pythonanywhere ya que la misma no posee soporte funcional para MySQL, lo resolvimos cambiando la arquitectura del programa usando ngrok y "reverse proxy", de esta manera solucionamos de manera eficiente el problema del despliegue de la aplicación y se puede consumir con una configuración particular toda la aplicación (PC y App Mobile).

Otra de las problematicas que surgieron fue por ejemplo pasar una variable de un template a otro template, la solución que encontramos fue enviarlo en un formulario oculto utilizando como valor la variable convertida a json. Esto se utilizó en el template de "metodoPago" para enviar la información de la variable diccionario "detallesEnvio" al endpoint de "confirmarCompra". A su vez repetimos el procedimiento en el "confirmarCompra" donde pasamos otro formulario oculto con la información de los formularios "detallesEnvio, metodoPago" y tambien la lista de productos que se encontraban en el carrito del almacenamiento local (LocalStorage).

Nos sentimos satisfechos, no solo por el resultado que logramos, sino por el compromismo que brindó el equipo habiendo un compañerismo ante las distintas dificultades atravesadas, nos pudimos ayudar entre nosotros y sumando experiencia en lo que es el trabajo en equipo. 

Finalmente, el TP fue desafiante ya que se tuvieron que estudiar algunas herramientas de forma autodidacta ya que no fueron provistas por la catedra (Vease Kivy, LocalStorage, ngrok) las cuales se podria incluir en futuras ediciones ya que facilitarian el desarrollo y desempeño de los equipos, pero el esfuerzo entregado valió la pena porque con esto conseguimos experiencia ya que salimos de nuestra zona de comfort extendiendo nuestro aprendizaje. 




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

