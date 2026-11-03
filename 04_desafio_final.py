# Datos iniciales que debes declarar 
nombre_producto = "Cuaderno"
precio_unitario = 2500
cantidad = 3
disponible = True
dinero_cliente = 10000
precio_total = precio_unitario * cantidad
descuento =  precio_total * 0.1
precio_final = precio_total - descuento
dinero_restante = dinero_cliente - precio_final
print(f'''Nombre: {nombre_producto}
precio: {precio_unitario}
cantidad disponible: {cantidad}
disponibilidad del producto: {disponible}
subtotal: {precio_unitario * cantidad}$
descuento: {descuento}$
total a pagar: {precio_final}$
dinero restante de cliente: {dinero_restante}$
''')
print(type(nombre_producto))
print(type(precio_unitario))
print(type(cantidad))
