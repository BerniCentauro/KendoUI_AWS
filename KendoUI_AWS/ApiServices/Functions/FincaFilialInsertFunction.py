import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def InsertNewFincaFilial(event, context):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("FincaFilial")
    
    try:

        table.put_item(Item = { 
                    'Id': event['Id'],
                    'Status' : event['Status'],
                    'NumberProperty' : event['NumberProperty'],
                    'IdCondominio' : event['IdCondominio'],
                    'IdUser' : event['IdUser']
                    })
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return ({"Resultado" : "Se han ingresado los datos correctamente"})