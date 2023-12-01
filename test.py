from app import*
#test para verificar que se obtiene el contacto de una cuenta (éxito)
def test_get_contactos():
    with app.test_client() as c:
        resp = c.get('/billetera/contactos/21345')
        assert resp.status_code == 200
        assert resp.json == {'123': 'Luisa', '456': 'Andrea'}
#test para verificar que de se puede hacer una transaccion a la misma cuenta(error ya que no hay una condicion que lo valide) 
def test_pagar():
    with app.test_client() as c:
        resp = c.get('/billetera/pagar/21345/21345/100')
        assert resp.status_code == 200
        assert resp.data == "Realizado en 30/11/2023."
#test para verificar que se puede hacer una transaccion con un saldo negativo (error)
def test_pagarneg():
    with app.test_client() as c:
        resp = c.get('/billetera/pagar/21345/456/-100')
        assert resp.status_code == 200
        assert resp.data == "Realizado en 30/11/2023."