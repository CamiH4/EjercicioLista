from turtle import pos, position
from Clases import Estudiante as est, ListadoEst as lst
import os
listaEst = lst()

def menu():
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Mostrar Registro")
    print("5. Buscar por Codigo")
    print("6. Buscar por Nombres")
    print("7. Buscar por Apellidos")
    print("8. Buscar por Carrera")
    print("9. Mostrar Cantidad de Estudiantes Becados")
    print("10. Salir")
    op = int(input("Escriba su opcion: "))
    return op

def agregarRegistro():
    os.system('cls')
    print("Agregar datos del Estudiante")
    codigo = input("Codigo: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    resp = input("Posee beca? SI - NO: ")
    print("="*40)
    if(resp.upper() == "SI"): beca = True
    else: beca = False
    estudiante = est(codigo, nombres, apellidos, carrera, beca)
    print(estudiante)
    print("="*40)
    listaEst.agregarElemento(estudiante)


def modificarregistro():
    os.system('cls')
    print("Editar Registro")
    cod = input("Codigo: ")
    estu, pos = listaEst.buscarCod(cod)
    print(f"""Nombres actual: {estu.Nombres}
Apellidos actual: {estu.Apellidos}
Carrera: {estu.Carrera}
Beca: {estu.Becado}""")
    print("Nuevos datos ")
    nuevoNombres = input("Nombres: ")
    nuevoApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    resp = input("Posee beca? SI - NO: ")
    if(resp.upper() == "SI"): nuevaBeca = True
    else: nuevaBeca = False
    newEst = est(estu.Codigo, nuevoNombres, nuevoApellidos, nuevaCarrera, nuevaBeca)
    listaEst.editarElemento(newEst, pos)
    print("="*40)

def eliminarRegistro():
    os.system('cls')
    print("Eliminar Registro")
    cod = input("Codigo: ")
    estu, pos = listaEst.buscarCod(cod)
    print(f"""Realmenete desea eliminar el registro {estu}""")
    resp = input("SI - NO: ")
    if resp.upper() == "SI":
        listaEst.eliminarElemento(estu)
    else:
        print("Operacion cancelada")
    print("="*40)
    
def buscarCodigo():
    os.system('cls')
    print("Buscar Codigo")
    cod = input("Codigo: ")
    try:
         est, pos = listaEst.buscarCod(cod)
         if est.Codigo != None:
             print(est)
    except Exception as ex:
        print("Sigue adelante")
        print("="*40)

def buscarNombre():
    os.system('cls')
    print("Buscar Nombres")
    nombre = input("Nombres: ")
    try:
         est, pos = listaEst.buscarNom(nombre)
         if est.Nombres != None:
             print(est)
    except Exception as ex:
        print("Sigue adelante")
        print("="*40)

def buscarApellido():
    os.system('cls')
    print("Buscar Apellidos")
    apellidos = input("Apellidos: ")
    try:
         est, pos = listaEst.buscarApe(apellidos)
         if est.Apellidos != None:
             print(est)
    except Exception as ex:
        print("Sigue adelante")
        print("="*40)

def buscarCarrera():
    os.system('cls')
    print("Buscar Carrera")
    carrera = input("Carrera: ")
    try:
         est, pos = listaEst.buscarCar(carrera)
         if est.Carrera != None:
             print(est)
    except Exception as ex:
        print("Sigue adelante")
        print("="*40)

def buscarBecas():
    os.system('cls')
    if listaEst.lista == []:
        print("No hay ningun estudiante registrado")
    else:
        cBeca = 0
        noBeca = 0
        for est in listaEst.lista:
            if est.Becado == True:
                cBeca +=1
            else:
                noBeca +=1
        print(f'Numero de estudiantes becados: {cBeca}')
        print(f'Numero de estudiantes no becados: {noBeca}')
    
def mostrarRegistros():
    os.system('cls')
    for est in listaEst.lista:
        print(est)
        print("="*40)

def main():
    op = 0 
    while( op!= 9):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarregistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: mostrarRegistros()
        elif op == 5: buscarCodigo()
        elif op == 6: buscarNombre()
        elif op == 7: buscarApellido()
        elif op == 8: buscarCarrera()
        elif op == 9: buscarBecas()
        elif op == 10: print("Adios...")
        else: print("Opcion invalida...")

main()