import MainServices
#import UserTable
#import CondoTable
#import FincaFilialTable

#----------Tabla Usuario----------#
#Paso 1 - Crear tabla y precargar la información:
#userTable = UserTable.UserTable
#userTable.CreateTable()
#userTable.InsertData()

#----------Tabla Condominio----------#
#Paso 2 - Crear tabla y precargar la información:
#condoTable = CondoTable.CondoTable
#condoTable.CreateTable()
#condoTable.InsertData()

#----------Tabla Finca Filial----------#
#Paso 3 - Crear tabla y precargar la información:
#fincaFilialTable = FincaFilialTable.FincaFilialTable
#fincaFilialTable.CreateTable()
#fincaFilialTable.InsertData()

#----------Iniciar Servicios----------#
#Paso 4 - Iniciar servicios:
mainServ = MainServices.MainServices
mainServ.runServices()