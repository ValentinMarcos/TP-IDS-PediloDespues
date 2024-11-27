from api import ver_productos, agregar_producto, producto_by_id

def test_ver_productos():
    productos = ver_productos()
    assert productos is not None, "La consulta de productos falló"
    assert len(productos) > 0, "No se encontraron productos"

def test_agregar_producto():
    nuevo_producto = {
        'Descripcion': 'Producto de Prueba',
        'Precio': 10.99,
        'Categoria': 'Prueba'
    }
    result = agregar_producto(nuevo_producto)
    assert result is not None, "La inserción del producto falló"
    assert result == 1, "No se insertó ningún producto"

def test_producto_by_id():
    descripcion = 'Producto de Prueba'
    producto = producto_by_id(descripcion)
    assert producto is not None, "La consulta del producto por ID falló"
    assert len(producto) > 0, "No se encontró el producto esperado"

if __name__ == "__main__":
    test_agregar_producto()
    test_ver_productos()
    test_producto_by_id()
    print("Todas las pruebas pasaron correctamente.")