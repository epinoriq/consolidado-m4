
bd_auto = []

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

    def insertar_auto(marca, modelo, nro_ruedas, velocidad, cilindrada):
        bd_auto.append({'Marca': marca, 'Modelo': modelo, 'Nro_rueda': nro_ruedas, 'Velocidad': velocidad, 'cilindrada': cilindrada})

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puesto = nro_puesto

    def ingreso_part(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto):
        bd_auto.append({'Marca': marca, 'Modelo': modelo, 'Nro_rueda': nro_ruedas, 'Velocidad': velocidad, 'cilindrada': cilindrada, 'Nro_puesto': nro_puesto})
    
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def ingreso_carga(marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        bd_auto.append({'Marca': marca, 'Modelo': modelo, 'Nro_rueda': nro_ruedas, 'Velocidad': velocidad, 'cilindrada': cilindrada, 'Peso_carga': peso_carga})

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def ingreso_bicicleta(marca, modelo, nro_ruedas, tipo_bicicleta):
        bd_auto.append({'Marca': marca, 'Modelo': modelo, 'Nro_rueda': nro_ruedas, 'Tipo_bicicleta': tipo_bicicleta})

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radio):
        super().__init__(marca, modelo, nro_ruedas, tipo_bicicleta)
        self.nro_radio = nro_radio
        self.cuadro = cuadro
        self.motor = motor

    def ingreso_motocicleta(marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radio):
        bd_auto.append({'Marca': marca, 'Modelo': modelo, 'Nro_rueda': nro_ruedas, 'Tipo_bicicleta': tipo_bicicleta, 'Motor': motor, 'Cuadro': cuadro, 'Nro_radio': nro_radio})

def modulo_ingreso():
    try:
        opcion = int(input("Elija una opción /n 1. Ingresar vehiculos /n 2. Consultar instancia motociclista :"))
        if opcion==1:
            cant_auto = int(input("Cuantos vehiculos desea ingresar: "))

            for contador in range(cant_auto):
                contador = contador + 1
                print(f"Datos del vehiculo {contador}")
                tipo_vehiculo = int(input("Ingrese el tipo de vehiculo 1. Automovil / 2.Bicicleta : "))
                marca = input("Inserte la marca del vehiculo: ")
                modelo = input("Inserte el modelo: ")
                nro_ruedas = int(input("Inserte el número de ruedas: "))
                if tipo_vehiculo==1:
                    velocidad = int(input("Inserte la velocidad en km/h: "))
                    cilindrada = input("Inserte el cilindraje en cc: ")
                    tipo_auto = int(input("Inserte la opcion del tipo de automovil, 1, si es Particular o 2 si es de Carga : "))
                    if tipo_auto== 1:
                        nro_puesto = int(input("Inserte los numeros de puestos: "))
                        Particular.ingreso_part(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto)
                    else:
                        peso_carga = input("Inserte la cantidad de peso de carga: ")
                        Carga.ingreso_carga(marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga)
                elif tipo_vehiculo==2:
                    tipo_motorizado = int(input("Ingrese el tmodalidad es 1. Bicicleta / 2. Motocicleta : "))
                    tipo_bicicleta = int(input("Ingrese el tipo de Bicicleta es : "))

                    if tipo_motorizado==1:
                        Bicicleta.ingreso_bicicleta(marca, modelo, nro_ruedas, tipo_bicicleta)
                    elif tipo_motorizado==2:
                        motor = input("Ingrese el motor: ")
                        cuadro = input("Ingrese el tipo de cuadro: ")
                        nro_radio = int(input("Ingrese el numero de radio: "))
                        Motocicleta.ingreso_motocicleta(marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radio)
            imprimir_ingreso()
        elif opcion==2:
            consulta_instancia()
        else:
            print("por favor ingresar una de las opciones indicadas")
            modulo_ingreso()
    except ValueError:
        print("Por favor ingresar solo numeros")

def imprimir_ingreso():
                        
        print("----------------------------------------------------------------------------------------")
        print("Imprimiendo por pantalla los vehículos ")
        print("")
        #print(bd_auto)
        for contador2 in range(len(bd_auto)):
            bd_contador = contador2 #Indico un contador para los registros de la lista
            contador2 = contador2 + 1 #Indico contador para los registros.
            n1 = bd_auto[bd_contador]
            if 'Tipo_bicicleta' in n1:
                #Busco si es una bicicleta o una motocicicleta
                if 'Motor' in n1:
                    print(f"Datos del vehiculo {contador2} : Marca {n1.get('Marca')} , Modelo {n1.get('Modelo')}, {n1.get('Nro_rueda')} ruedas  Tipo: {n1.get('Tipo_bicicleta')} Motor: {n1.get('Motor')}, Cuadro: {n1.get('Cuadro')}, Nro Radio {n1.get('Nro_radio')}")
                    #print("Este registro es una moto")
                elif 'Motor' not in n1:
                    print(f"Datos del vehiculo {contador2} : Marca {n1.get('Marca')} , Modelo {n1.get('Modelo')}, {n1.get('Nro_rueda')} ruedas  Tipo: {n1.get('Tipo_bicicleta')}")
                    #print("Este registro es una bicicleta")
            elif 'Tipo_bicicleta' not in n1:
                #Busco si es un automovil particular o de carga
                if 'Peso_carga' in n1:
                    print(f"Datos del vehiculo {contador2} : Marca {n1.get('Marca')} , Modelo {n1.get('Modelo')}, {n1.get('Nro_rueda')} ruedas {n1.get('Velocidad')} km/h {n1.get('cilindrada')} cc Carga: {n1.get('Peso_carga')} kg")
                    #print("Este registro es un vehiculo de carga")
                elif 'Peso_carga' not in n1:
                    print(f"Datos del vehiculo {contador2} : Marca {n1.get('Marca')} , Modelo {n1.get('Modelo')}, {n1.get('Nro_rueda')} ruedas {n1.get('Velocidad')} km/h {n1.get('cilindrada')} cc Puestos: {n1.get('Nro_puesto')}")
                    #print("Este registro es un vehiculo particular")
            print("")
        print("----------------------------------------------------------------------------------------")
    
    
def consulta_instancia():
    consulta = Motocicleta('MW', 'KS', 2, 'Deportiva', '2T', 'Doble Viga', 21)
    print(f"Motocicleta es instancia con relación a Vehículo:  {isinstance(consulta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(consulta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(consulta, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de carga: {isinstance(consulta, Carga)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(consulta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(consulta, Motocicleta)}")


#--------------------------------INGRESO POR MEDIO DEL MODULO------------------------------------------
#modulo_ingreso()
#------------------------------------------------------------------------------------------------------
#--------------------------------CONSULTA INSTANCIA SIN ENTRAR AL MODULO-------------------------------
#consulta_instancia()
#------------------------------------------------------------------------------------------------------

#--------------------------------INGRESO POR DATO BRUTO------------------------------------------------
# Particular.ingreso_part('Ford', 'Fiesta', 4, 180, '500', 5)
# Carga.ingreso_carga('Daft Trucks', 'G 38', 10, 120, '1000', '20000')
# Bicicleta.ingreso_bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
# Motocicleta.ingreso_motocicleta('MW', 'KS', 2, 'Deportiva', '2T', 'Doble Viga', 21)
# imprimir_ingreso()
#------------------------------------------------------------------------------------------------------

