from librodiario import LibroDiario

libro = LibroDiario()

# Cargar desde archivo
libro.cargar_transacciones_desde_archivo("transacciones.csv")

print(libro.calcular_resumen())


#from librodiario import LibroDiario

#libro = LibroDiario()

#libro.agregar_transaccion('2025-06-19', 'Venta de disco SSD', 80, 'InGrEso') 
#libro.agregar_transaccion('2025-06-18', 'Compra de teclado Polaroid', 50, 'EGreSO')  
#libro.agregar_transaccion('2025-06-19', 'Venta de pantalla ENV', 200, 'ingreso') 
#libro.agregar_transaccion('2025-06-16', 'Compra de mouse Logitech', 100, 'egreso')  

# print(libro.calcular_resumen())

