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
        contactos = usuario['contactos']
        contacto_numero = {}
        
        print("A")
        
        for contacto in contactos:
            response1 = tabla.get_item(
                Key = {
                    'numero': contacto
                }    
            )
            print("B")
            contacto_numero[contacto] = response1.get('Item')['nombre']
            print("nuevo_contacto: ",contacto_numero[contacto])
        
        # print("contactos:",contactos)

        return {
            'statusCode': 200,
            'body': contacto_numero
        }
    except Exception as e:
        return{
            'statusCode': 500,
            'body': json.dumps("Error del servidor")
        }
