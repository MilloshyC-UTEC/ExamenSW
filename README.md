# ExamenSW
Pregunta 3
Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir
por día.
Qué cambiaría en el código (Clases / Métodos) - No implementación.
Nuevos casos de prueba a adicionar.
Cuánto riesgo hay de “romper” lo que ya funciona?

Respuesta:
Para hacer lo del cambio de soportar un valor maximo de 200 soles es necesario hacer un metodo en Cuenta para que verifique el monto que se quiere tranferir si se excede de 200 no hace la transaciones, lo que agreraria seria una funcion llamada transaccionvalidar() en que verifico si es mayor de 200 retorno un bool True para que no realize la transaccion, adicional a ello se tiene que verificar que esa transaccion sea por dia, otra opcion podria ser agregar un atributo en la clase Operacion en el que contendra un bool para validar una transaccion de pago, el nuevo caso de prueba seria validar de que si hago una transaccion mayor de 200 mi api deberia rechazar esa transaccion y de esa forma me aseguro de que funciona correctamente, no se tendria tanto riesgo ya que solo se trata de validar el monto de transacion :)
