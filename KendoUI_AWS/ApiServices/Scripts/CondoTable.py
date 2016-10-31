import boto3
import traceback

class CondoTable:

    #Metodo para crear la tabla de condominios.
    def CreateTable():

        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

        try:
            table = dynamodb.create_table(TableName='Condominio',
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
        table = dynamodb.Table('Condominio')

        try:
            table.put_item(Item = { 
                    'Id': '1',
                    'Logo' : 'logo1.png',
                    'Description' : 'Información general del condominio',
                    'PageUrl' : 'www.test.com'
                    })

            table.put_item(Item = { 
                    'Id': '2',
                    'Logo' : 'logo2.png',
                    'Description' : 'Información general del condominio',
                    'PageUrl' : 'www.test.com'
                    })

        except Exception:
            print("Ha ocurrido un error")
            traceback.print_exc()

        else:
            print("Datos ingresados correctamente")