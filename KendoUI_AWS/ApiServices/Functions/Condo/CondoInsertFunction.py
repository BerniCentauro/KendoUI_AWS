﻿import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def InsertNewCondo(event, context):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Condominio")
    
    try:
        table.put_item(Item = {
            'Id': event['Id'],
            'Description' : event['Description'],
            'Logo' : event['Logo'],
            'PageUrl' : event['Url']
            })
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return ({"Resultado" : "Se han ingresado los datos correctamente"})