import boto3
import traceback

class FiancaFilialTable():

    #Metodo para creacion de la tabla FincaFilial
    def createTableFincaFilial():
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        try:
            fincaTable = dynamodb.create_table(TableName='FincaFilial',
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

    def insertData():

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
        tableFincaFilial = dynamodb.Table('FincaFilial')


        try:
           tableFincaFilial.put_item(Item = { 
                    'Id': '1',
                    'Status' : 'true',
                    'NumberProperty' : '12345',
                    'IdCondominio' : '1',
                    'IdUser' : '1'
                    })

            tableFincaFilial.put_item(Item = { 
                    'Id': '1',
                    'Status' : 'true',
                    'NumberProperty' : '12345',
                    'IdCondominio' : '1',
                    'IdUser' : '1'
                    })

        except:
            print("Ha ocurrido un error al precargar los datos de la tabla FincaFilial")
        else: 
            print("Datos precargados correctamente")
