# EF_SW

# Pregunta 1

## API de contactos

Método POST
https://jmyqdgd43c.execute-api.us-east-1.amazonaws.com/nuevo/billetera/contactos

JSON:

{
  "numero": "99999999"
}

## API de pago

Método POST
https://jmyqdgd43c.execute-api.us-east-1.amazonaws.com/nuevo/billetera/pagar

JSON:

{
  "numero_emisor": "99999999",
  "numero_receptor": "88888888",
  "monto": 5,
  "tipo_operacion": "envio"
}

## API de historial

Método POST
https://jmyqdgd43c.execute-api.us-east-1.amazonaws.com/nuevo/billetera/historial

JSON:

{
  "numero": "99999999"
}


# Pregunta 3
Requisito: valor máximo de transferencia, 200 soles por día

Se implementaría un método que sume los montos de las transferencias que realizó dicho usuario para el mismo día. Si dicha suma es mayor a 200 soles, no permite realizar la transferencia. Si el monto a transferir es mayor a 200 soles, no debería permitir la transferencia. 

Los casos de pruebas serían:
- que se intente transferir más de 200 soles
- que la suma de transferencias sea mayor a 200 soles en el mismo día

Sí, estos verifican que las funcionalidades actuales trabajen de manera correcta. 
- No permite transferencias cuando el usuario no tiene saldo suficiente
- no permite transferir a no contactos
- el emisor debe existir. 
