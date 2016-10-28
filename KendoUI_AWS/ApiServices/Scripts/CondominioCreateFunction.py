import boto3
import traceback

class CreateTableCondominio:

    def CondominioCreateTable():

        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

        table = dynamodb.create_table(TableName='Condominio',
                                      keySchema=[{
                                          'AttributeName': 'Id',
                                          'KeyType': HASH
                                          }],
                                      AttributeDefinitions=[{
                                          'AttributeName': 'Id',
                                          'AttributeType': 'S'
                                          }],
                                      ProvissionedThroughput=
                                      {
                                          'ReadCapacityUnits': 5,
                                          'WriteCapacityUnits': 5
                                          })

        print(table.item_count)
        print("Tabla creada correctamente")

        CondominioCreateTable()