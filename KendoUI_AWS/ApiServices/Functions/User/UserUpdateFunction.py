import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def UpdateUser(event, context):

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("User")
    
    try:

        response = table.update_item(Key = {"Id" : event["Id"]},
            UpdateExpression = "Set Email = :valEmail, Password = :valPass, Username = :valName, Phone = :valPhone, Identification = :valIdent",
            ExpressionAttributeValues = {
                ":valEmail": event["Email"],
                ":valPass" : event["Password"],
                ":valName" : event["Username"],
                ":valPhone" : event["Phone"],
                ":valIdent" : event["Identification"]
                },
            ReturnValues = "UPDATED_NEW")
        
    except ClientError as e:
        print(e.response["Error"]["Message"])
        return ({"Resultado" : "Ha ocurrido un error"})
        
    else:
        return (response)