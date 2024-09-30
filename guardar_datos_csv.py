from Vehiculo import Particular, Carga, Bicicleta, Motocicleta
import csv

def guardar(nombre_archivo, Particular, Carga, Bicicleta, Motocicleta):
    archivo = open(nombre_archivo, "w")
    #datos = [(Particular.__class__, Particular.__dict__, Carga.__class__, Carga.__dict__, Bicicleta.__class__, Bicicleta.__dict__, Motocicleta.__class__, Motocicleta.__dict__)]
    datos = [(Particular.__class__, Particular.__dict__)]
    datos1 = [(Carga.__class__, Carga.__dict__)]
    datos2 = [(Bicicleta.__class__, Bicicleta.__dict__)]
    datos3 = [(Motocicleta.__class__, Motocicleta.__dict__)]
    archivo_csv = csv.writer(archivo, lineterminator='\n')
    archivo_csv.writerows(datos)
    archivo_csv.writerows(datos1)
    archivo_csv.writerows(datos2)
    archivo_csv.writerows(datos3)
    archivo.close()

def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
        archivo.close()
        return vehiculos

particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

guardar("vehiculos.csv", particular, carga, bicicleta, motocicleta)

carga_datos = open("vehiculos.csv")
contenido = carga_datos.read()
print(contenido)