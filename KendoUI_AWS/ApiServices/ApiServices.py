import UserTable
import UserServices

import CondoTable
import CondoServices

#----------Tabla Usuario----------#
#Paso 1 - Crear tabla y precargar la información:
#userTable = UserTable.UserTable
#userTable.CreateTable()
#userTable.InsertData()

#Paso 2 - Iniciar servicios:
#userServices = UserServices.UserServices
#userServices.runServices()

#----------Tabla Condominio----------#
#Paso 1 - Crear tabla y precargar la información:
#condoTable = CondoTable.CondoTable
#condoTable.CreateTable()
#condoTable.InsertData()

#Paso 2 - Iniciar servicios:
condoServices = CondoServices.CondoServices
condoServices.runServices()

#----------Tabla Finca Filial----------#