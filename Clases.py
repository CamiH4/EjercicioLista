# Crear una lista de estudiantes
"""Create
READ
Update
Delete"""

class Estudiante:

    def __init__(self, cod, nom, ape, car, bec):
        # Se pone en mayuscula las propiedades
        self.Codigo = cod
        self.Nombres = nom
        self.Apellidos = ape
        self.Carrera = car
        self.Becado = bec #Becado sera un valor booleano
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Apellidos: {self.Apellidos}
Carrera: {self.Carrera}
Beca: {self.Becado}
        """

class ListadoEst:

    def __init__(self): #Se puede elemento o valor
        self.lista = []
    
    def agregarElemento(self, elem):
        try:
            self.lista.append(elem)
        except Exception as ex:
            print("Ocurrio un error al agregar", str(ex))
    
    def editarElemento(self, elem, pos):
        try:
            self.lista[pos] = elem
        except Exception as ex:
            print("Ocurrio un error al editar.", str(ex))
    
    def eliminarElemento(self, est):
        try:
            self.lista.remove(est)
        except Exception as ex:
            print("Ocurrio un error al eliminar", str(ex))
    
    def buscarCod(self, codigo):
        try:
            pos = 0
            for est in self.lista:
                if est.Codigo == codigo:
                    print("Estudiante encontrado...")
                    return est, pos
                    pos += 1
            else:
                print("No se encontro...")
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

    def buscarNom(self, nom):
        try:
            pos = 0
            for est in self.lista:
                
                if est.Nombres == nom:
                    print("Estudiante encontrado...")
                    return est, pos
                    pos += 1
            else:
                print("No se encontro...")
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

    def buscarApe(self,ape):
        try:
            pos = 0
            for est in self.lista:
                if est.Apellidos == ape:
                    print("Estudiante encontrado...")
                    return est, pos    
                    pos += 1
            else:
                print("No se encontro...")
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

    def buscarCar(self, car):
        try:
            pos = 0
            for est in self.lista:
                if est.Carrera == car:
                    print("Estudiante encontrado...")
                    return est, pos
                    pos += 1
            else:
                print("No se encontro...")
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))


    