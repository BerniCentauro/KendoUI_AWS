import boto3
import traceback

class FincaFilialTable:

    #Metodo para crear la tabla FincaFilial.
    def CreateTable():

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        try:
            table = dynamodb.create_table(TableName='FincaFilial',
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
        table = dynamodb.Table('FincaFilial')

        try:
            table.put_item(Item = { 
                    'Id': '1',
                    'Status' : 'true',
                    'NumberProperty' : '12345',
                    'IdCondominio' : '1',
                    'IdUser' : '1'
                    })

            table.put_item(Item = { 
                    'Id': '1',
                    'Status' : 'true',
                    'NumberProperty' : '12345',
                    'IdCondominio' : '1',
                    'IdUser' : '1'
                    })

        except Exception:
            print("Ha ocurrido un error")
            traceback.print_exc()

        else:
            print("Datos ingresados correctamente")


