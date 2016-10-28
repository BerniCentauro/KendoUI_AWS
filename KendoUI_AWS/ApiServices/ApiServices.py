import FincaFilialTable


#----------Tabla Usuario----------#
#Paso 1 - Inicializar script para la base de datos
fincaFilialTable = FincaFilialTable.FincaFilialTable

#Paso 2 - Crear tabla:
fincaFilialTable.CreateTable()

#Paso 3 - Precargar usuarios en la tabla:
fincaFilialTable.InsertData()

#Paso 4 - Iniciar servicios:
#userServices = UserServices.UserServices
#userServices.runServices()

#----------Tabla Condominio----------#

#----------Tabla Finca Filial----------#

#ApiServices


