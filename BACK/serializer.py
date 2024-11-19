def serializador_productos(productos):
    
    productos_por_categoria = {}

    for producto in productos:
        id_producto, descripcion, precio, categoria = producto 
        
        if categoria not in productos_por_categoria:
            productos_por_categoria[categoria] = []
        
        
        descripcion_img = descripcion.lower().replace(" ", "")
        
        productos_por_categoria[categoria].append({
            'nombre': descripcion,
            'img': f"static/images/{descripcion_img}.jpg",  
            'precio': precio
        })

    return productos_por_categoria
