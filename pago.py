import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        tabla = dynamodb.Table("Contactos")
        
        numero_emisor = event["numero_emisor"]
        numero_receptor = event["numero_receptor"]
        monto = event["monto"]
        tipo_operacion = event["tipo_operacion"]  # 'envio' o 'recibo'
        fecha = datetime.now().strftime("%d/%m/%Y")
        
        # Obtener información del emisor
        response = tabla.get_item(
            Key={'numero': numero_emisor}
        )
        usuario = response.get('Item')
        
        print("A")
        
        if not usuario:
            return {
                "statusCode": 404,
                "body": json.dumps("Emisor no encontrado!")
            }
        
        saldo = usuario['saldo']
        
        if tipo_operacion == 'envio' and saldo < monto:
            return {
                "statusCode": 401,
                "body": json.dumps("Saldo insuficiente!")
            }
        
        # Actualizar historial y saldo del emisor
        if tipo_operacion == 'envio':
            nuevo_saldo = saldo - monto
            historial_update = {
                "fecha": fecha,
                "monto": monto,
                "tipo": "envio"
            }
        else:
            nuevo_saldo = saldo + monto
            historial_update = {
                "fecha": fecha,
                "monto": monto,
                "tipo": "recibo"
            }
        
        tabla.update_item(
            Key={'numero': numero_emisor},
            UpdateExpression="SET historial = list_append(historial, :historial), saldo = :nuevo_saldo",
            ExpressionAttributeValues={
                ':historial': [historial_update],
                ':nuevo_saldo': nuevo_saldo
            }
        )
        
        return {
            'statusCode': 200,
            'Realizado en': fecha
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error del servidor: {str(e)}")
        }
