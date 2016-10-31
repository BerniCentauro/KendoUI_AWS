import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def GetFincaFilialById(event, context):
    
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("FincaFilial")
    
    try:
        response = table.get_item(Key = { "Id": event["Id"] })
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return (response)