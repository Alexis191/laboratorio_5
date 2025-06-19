from librodiario import LibroDiario

libro = LibroDiario()

libro.agregar_transaccion('2025-06-19', 'Venta de disco SSD', 80, 'InGrEso') 
libro.agregar_transaccion('2025-06-18', 'Compra de teclado Polaroid', 50, 'EGreSO')  
libro.agregar_transaccion('17/06/2025', 'Venta de pantalla ENV', 200, 'ingreso') 
libro.agregar_transaccion('2025-06-16', 'Compra de mouse Logitech', 100, 'gasto')  

print(libro.calcular_resumen())
