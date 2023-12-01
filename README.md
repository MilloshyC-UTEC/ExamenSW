# ExamenSW
Pregunta 3
Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir
por día.
Qué cambiaría en el código (Clases / Métodos) - No implementación.
Nuevos casos de prueba a adicionar.
Cuánto riesgo hay de “romper” lo que ya funciona?
Respuesta:
Para hacer lo del cambio de soportar un valor maximo de 200 soles es necesario hacer un metodo en Cuenta para que verifique el monto que se quiere tranferir si se excede de 200 no hace la transaciones, lo que agreraria seria una funcion llamada montovalidar() en que verifico si es mayor de 200 retorno un bool True para que no realize la transaccion 
