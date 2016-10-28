import UserTable
import UserServices

import CondominioCreateTable

#----------Tabla Usuario----------#
#Paso 1 - Inicializar script para la base de datos
#userTable = UserTable.UserTable

#Paso 2 - Crear tabla:
#userTable.CreateTable()

#Paso 3 - Precargar usuarios en la tabla:
#userTable.InsertData()

#Paso 4 - Iniciar servicios:
userServices = UserServices.UserServices
userServices.runServices()

#----------Tabla Condominio----------#
#Paso 1 - Inicializar script para la base de datos
CondoTable = CondominioCreateTable.CondominioCreateTable

#Paso 2 - Crear tabla:
CondoTable.CondominioCreateTableFunction()

#Paso 3 - Precargar usuarios en la tabla:
#userTable.InsertData()

#Paso 4 - Iniciar servicios:
userServices = UserServices.UserServices
userServices.runServices()

#----------Tabla Finca Filial----------#