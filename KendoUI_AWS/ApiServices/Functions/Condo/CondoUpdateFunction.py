import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def UpdateCondo(event, context):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Condominio")
    
    try:

        response = table.update_item(Key = {"Id" : event["Id"]},
            UpdateExpression = "Set Description = :valDescription, Logo = :valLogo, PageUrl = :valUrl",
            ExpressionAttributeValues = {
                ":valDescription": event["Description"],
                ":valLogo" : event["Logo"],
                ":valUrl" : event["Url"]
                },
            ReturnValues = "UPDATED_NEW")
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return (response)