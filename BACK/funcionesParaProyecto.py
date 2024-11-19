def agregar_producto(data):
    result = run_query(QUERY_AGREGAR_PRODUCTO, data)
    if result:
        return result.rowcount
    return 0

def producto_by_id(Descripcion):
    result = run_query(QUERY_PRODUCTO_BY_ID, {'Descripcion': Descripcion})
    if result:
        return result.fetchall()
    return []

def agregar_ticket(total, carrito, estado = "Pendiente"):
    payload = str(carrito)
    ticket_id = (uuid.uuid4())
    fecha_creacion = datetime.now()
    params = {
        'ID': ticket_id,
        'Total': total,
        'Payload': payload,
        'Estado': estado,
        'FechaCreacion': fecha_creacion,
    }
    result = run_query(QUERY_AGREGAR_TICKET, params)
    if result:
        return ticket_id
    return 0

def ver_tickets():
    result = run_query(QUERY_VER_TICKETS)
    if result:
        return result.fetchall()
    return []
