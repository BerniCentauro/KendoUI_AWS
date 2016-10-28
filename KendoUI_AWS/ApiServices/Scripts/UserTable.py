import boto3
import traceback

class UserTable:

    #Metodo para crear la tabla usuarios.
    def CreateTable():

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        try:
            table = dynamodb.create_table(TableName='User',
                KeySchema=[{
                        'AttributeName': 'Id',
                        'KeyType': 'HASH'
                    }],
                AttributeDefinitions=[{
                        'AttributeName': 'Id',
                        'AttributeType': 'S'
                    }],
                ProvisionedThroughput=
                {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                })

        except Exception:
            print("Ha ocurrido un error")
            traceback.print_exc()

        else:
            print(table.creation_date_time)
            print("Tabla creada correctamente")

    #def InsertData():

    #    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
    #    table = dynamodb.Table("User")

    #    try:
    #        table.put_item(Item = { 
    #                "Id": event["Id"],
    #                "Email" : event["Name"],
    #                "Lastname" : event["Lastname"],
    #                "Email" : event["Email"]
    #                })

    #    except Exception:
    #        print("Ha ocurrido un error")
    #        traceback.print_exc()

    #    else:
    #        print("Datos ingresados correctamente")
        