import json
import boto3

def lambda_handler(event, context):
    
    try:
        dynamodb = boto3.resource("dynamodb")
        tabla = dynamodb.Table("Contactos")
        # TODO
        
        response = tabla.get_item(
            Key={
                'numero': event["numero"]
            }
        )
        usuario = response.get('Item')
        saldo = usuario['saldo']
        nombre = usuario['nombre']
        historial = usuario['historial']
        
        # print("contactos:",contactos)

        return {
            'statusCode': 200,
            'nombre': nombre,
            'saldo': saldo,
            'operaciones': historial
        }
    except Exception as e:
        return{
            'statusCode': 500,
            'body': json.dumps("Error del servidor")
        }
