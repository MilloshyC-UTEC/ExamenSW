from clases import*
from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)
Cuenta1=Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
Cuenta2=Cuenta('123', 'Luisa', 400, ['456'])
Cuenta3=Cuenta('456', 'Andrea', 300, ['21345'])
BD = [Cuenta1,Cuenta2,Cuenta3]
@app.route('/billetera/contactos/<string:numero>')
def get_contactos(numero):
    result={}
    for cuenta in BD:
        if cuenta.getnumero() == numero:
            for contacto in cuenta.getcontactos():
                for cuenta in BD:
                    if cuenta.getnumero() == contacto:
                        result[cuenta.getnumero()]=cuenta.getnombre()
    return jsonify(result)

@app.route('/billetera/pagar/<string:numero>/<string:numdestino>/<int:valor>')
def pagar(numero, numdestino, valor):
    cuentas = [Cuenta1, Cuenta2, Cuenta3]
    for cuenta in cuentas:
        if cuenta.getnumero() == numero:
            if cuenta.realizar_pago(numdestino, valor, cuentas):
                return f"Realizado en {datetime.now().strftime('%d/%m/%Y')}."
            else:
                return "Saldo insuficiente."
    return "Cuenta no encontrada."

@app.route('/billetera/historial/<string:numero>')
def historial(numero):
    cuentas = [Cuenta1, Cuenta2, Cuenta3]
    for cuenta in cuentas:
        if cuenta.getnumero() == numero:
            saldo = cuenta.getsaldo()
            operaciones = cuenta.get_historial()
            return jsonify("Saldo de {}: {} Operaciones de {} {}".format(cuenta.getnombre(), saldo, cuenta.getnombre(), ', '.join(operaciones)) if operaciones else "No hay operaciones registradas."
)


    return jsonify("Cuenta no encontrada.")

    
    
if __name__ == '__main__':
    app.run(debug=True)
