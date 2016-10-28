import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def UpdateFincaFilial(event, context):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("FincaFilial")
    
    try:

        response = table.update_item(Key = {"Id" : event["Id"]},
            UpdateExpression = "Set Status = :valStatus, NumberProperty = :valNumberProperty, IdCondominio = :valIdCondominio, IdUser = :valIdUser",
            ExpressionAttributeValues = {
                ":valStatus": event["Status"],
                ":valNumberProperty" : event["NumberProperty"],
                ":valIdCondominio" : event["IdCondominio"],
                ":valIdUser" : event["IdUser"]
                },
            ReturnValues = "UPDATED_NEW")
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return (response)