WAREHOUSE = [
    {
        "code": "A001",
        "producto": "pan",
        "price": 1.5
    },
    {
        "code": "A002",
        "producto": "leche",
        "price": 2.5
    }
]

def show_menu():
    print("""
    1. Ver catálogo
    2. Agregar producto al carrito
    3. Eliminar producto del carrito
    4. Vaciar carrito
    5. Mostrar carrito
    6. Finalizar compra
    7. Salir      
    """)

def show_catalog():
    print(f"{'Código':<8} | {'Nombre':<10} | {'Precio':<8}")
    print("-" * 30)
    for product in WAREHOUSE:
        print(f"{product['code']:<8} | {product['producto']:<10} | S/.{product['price']:<6.2f}")
    
# show_menu()
show_catalog()    
