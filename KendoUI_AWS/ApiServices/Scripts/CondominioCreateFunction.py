import boto3
import traceback

class CreateTableCondominio:

    #Metodo para crear la tabla usuarios.
    def CondominioCreateTable():

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