FILE_NAME = 'ventas.txt'

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

SHOPPING_CAR = []

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
        
def add_product_to_shopping_car(code_product):
    for product in WAREHOUSE:
        if code_product == product["code"]:
            SHOPPING_CAR.append(product)
            print(f"El producto {product['code']} fue agregado al carrito")
            break
    

def add_order_to_file(registerd_at, list_products, total_price):
    complete_order = '=====================================\n\n'
    complete_order += f"Fecha: {registerd_at}\n\n"
    
    for prod in list_products:
        complete_order += f"{prod.get('quantity')}  |  {prod['producto']} \n"
    
    complete_order += f"S/. {total_price}\n\n"
    complete_order += '=====================================\n' 
    
    with open(FILE_NAME, 'a') as archivo:
        archivo.write(complete_order)    
    
    
def remove_from_shopping_car():
    pass

def empty_shopping_car():
    pass
    
def finalize_purchase():
    pass    

def main():
    pass
    
show_menu()
show_catalog()
print("\n")     
add_order_to_file(
    "01-05-2025 10:59:50",
    [{
        "quantity": 1,
        "code": "A001",
        "producto": "pan",
        "price": 1.5
    },
    {
        "quantity": 1,
        "code": "A002",
        "producto": "leche",
        "price": 2.5
    }],
    4.0
)
