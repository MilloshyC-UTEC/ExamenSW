import datetime

class Operacion:
    def __init__(self, numero_origen: str, numero_destino: str, valor: int):
        self.numero_origen = numero_origen
        self.numero_destino = numero_destino
        self.fecha = datetime.datetime.now()
        self.valor = valor
class Cuenta:
    def __init__(self,numero,nombre,saldo,contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = int(saldo)
        self.contactos =contactos
        self.pagos_realizados = []
        self.pagos_recibidos = []

    def getinfo(self):
        return {self.numero:self.nombre}
    def getnumero(self):
        return (self.numero)
    def getnombre(self):
        return self.nombre
    def getsaldo(self):
        return self.saldo
    def getcontactos(self):
        return self.contactos
    def realizar_pago(self, num_destino, valor, cuentas):
        if self.saldo >= valor:
            self.saldo -= valor
            operacion = Operacion(self.numero, num_destino, valor)
            self.pagos_realizados.append(operacion)
            for cuenta in cuentas:
                if cuenta.getnumero() == num_destino:
                    cuenta.saldo += valor
                    cuenta.pagos_recibidos.append(operacion)
            return True
        else:
            return False
    def get_historial(self):
        historial = []
        for operacion in self.pagos_realizados:
            historial.append(f"Pago realizado de {operacion.valor} a {operacion.numero_destino}")
        for operacion in self.pagos_recibidos:
            historial.append(f"Pago recibido de {operacion.valor} de {operacion.numero_origen}")
        return historial
