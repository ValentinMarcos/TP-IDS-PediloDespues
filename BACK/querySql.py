from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

class Query_sql:
    PRODUCTOS_GET_ALL = "SELECT * FROM Productos"
    PRODUCTOS_GET_BY_ID = "SELECT Descripcion, Precio, Categoria FROM Productos WHERE Descripcion = :Descripcion"
    PRODUCTOS_ADD = "INSERT INTO Productos (Descripcion, Precio, Categoria) VALUES (:Descripcion, :Precio, :Categoria)"
    TICKET_GET_ALL = "SELECT * FROM Tickets"
    TICKET_BY_ID = "SELECT ID, Total, Payload, Estado, FechaCreacion FROM Tickets WHERE ID = :ID"
    ADD_TICKET = "INSERT INTO Tickets (ID, Total, Payload, Estado, FechaCreacion) VALUES (:ID, :Total, :Payload, :Estado, :FechaCreacion)"
    
    def ejecutarSQL(self, query, parameters=None):
        engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3306/proyecto")
        try:
            with engine.connect() as conn:
                result = conn.execute(text(query), parameters)
                conn.commit()  
                return result
        except SQLAlchemyError as e:
            print(f"Error en la consulta: {e}")
            return None