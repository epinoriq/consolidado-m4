class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def insertar_auto():
        cant_auto = int(input("Cuantos vehiculos desea ingresar: "))

        bd_auto = []

        try:
            for contador in range(cant_auto):
                contador = contador + 1
                print(f"Datos del vehiculo {contador}")
                marca = input("Inserte la marca del automóvil: ")
                modelo = input("Inserte el modelo: ")
                nro_rueda = int(input("Inserte el número de ruedas: "))
                velocidad = int(input("Inserte la velocidad en km/h: "))
                cilindrada = int(input("Inserte el cilindraje en cc: "))

                bd_auto.append([marca, modelo, nro_rueda, velocidad, cilindrada])

            print("----------------------------------------------------------------------------------------")
            print("Imprimiendo por pantalla los vehículos ")
            print("")
            for contador2 in range(len(bd_auto)):
                bd_contador = contador2 #Indico un contador para los registros de la lista
                contador2 = contador2 + 1 #Indico contador para los registros.
                n1 = bd_auto[bd_contador]
                print(f"Datos del automovil {contador2} : Marca {n1[0]} , Modelo {n1[1]}, {n1[2]} ruedas {n1[3]} km/h {n1[4]} cc ")
                print("")
            print("----------------------------------------------------------------------------------------")
        except ValueError:
            print("Por favor ingresar solo numeros")
    
    insertar_auto()
    










        

        
