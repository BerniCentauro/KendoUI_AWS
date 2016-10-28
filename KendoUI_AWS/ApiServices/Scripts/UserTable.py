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

    #Método para precargar información dentro de la tabla.
    def InsertData():

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
        table = dynamodb.Table('User')

        try:
            table.put_item(Item = { 
                    'Id': '1',
                    'Email' : 'user1@test.com',
                    'Password' : '12345',
                    'Username' : 'Test user 1',
                    'Phone' : '555-555',
                    'Identification' : '123'
                    })

            table.put_item(Item = { 
                    'Id': '2',
                    'Email' : 'user2@test.com',
                    'Password' : '12345',
                    'Username' : 'Test user 2',
                    'Phone' : '555-555',
                    'Identification' : '123'
                    })

        except Exception:
            print("Ha ocurrido un error")
            traceback.print_exc()

        else:
            print("Datos ingresados correctamente")
        