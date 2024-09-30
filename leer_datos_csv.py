
def main():
    carga_datos = open("vehiculos.csv", "r", encoding="utf-8")
    bd_linea = carga_datos.readlines(1)
    bd_linea1 = carga_datos.readlines(2)
    bd_linea2 = carga_datos.readlines(3)
    bd_linea3 = carga_datos.readlines(4)
    pri_linea = bd_linea[0]
    sec_linea = bd_linea1[0]
    tri_linea = bd_linea2[0]
    cua_linea = bd_linea3[0]
    base_cad = pri_linea[31:-2]
    base_cad_1 = sec_linea[31:-2]
    base_cad_2 = tri_linea[31:-2]
    base_cad_3 = cua_linea[31:-2]
    print("Lista de Vehiculos Particular ")
    print(base_cad)
    print("Lista de Vehiculos Carga")
    print(base_cad_1)
    print("Lista de Vehiculos Bicicleta ")
    print(base_cad_2)
    print("Lista de Vehiculos Motocicleta")
    print(base_cad_3)

    #print(f"Marca {resultado.get('marca')} , {resultado.get('modelo')}, {resultado.get('nro_ruedas')} ruedas {resultado.get('velocidad')} km/h {resultado.get('cilindrada')} cc Puestos: {resultado.get('nro_puesto')}")

    carga_datos.close()
main()
