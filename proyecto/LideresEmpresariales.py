from BaseDeDatos import BaseDeDatos 

class LideresEmpresariales():
    
    listaArgumentos = ['ceo','cto','mesaDirectiva','jefeDepartamento','empresa','presidente','accionistasMayoritarios']
    _listaObjetos = []

    @classmethod
    def regresarArgumentos(cls):
        return cls.listaArgumentos

    @classmethod
    def regresarObjeto(cls,argumento, nombreObjeto):
        for objeto in cls._listaObjetos:
            cadena = eval('objeto.'+argumento)
            if cadena == nombreObjeto: 
                return objeto

    @classmethod
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
       for arg in cls.listaArgumentos:
                if argumento == arg:
                    for obj in cls._listaObjetos:
                        if obj == objeto:
                            eval('cls._listaObjetos[cls._listaObjetos.index(obj)].'+argumento+' = dato')

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('LideresEmpresariales')
        for lista in listas:
            LideresEmpresariales(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('LideresEmpresariales',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.ceo = input('CEO: ')
            self.cto = input('CTO: ')
            self.mesaDirectiva = input('Mesa Directiva: ')
            self.jefeDepartamento = input('Jefe Departamento: ')
            self.empresa = input('Empresa: ')
            self.presidente = input('Presidente: ')
            self.accionistasMayoritarios = input('Accionistas Mayoritarios: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('LideresEmpresariales', [self.ceo,self.cto,self.mesaDirectiva,self.jefeDepartamento,self.empresa,self.presidente,self.accionistasMayoritarios], self.listaArgumentos)
        elif modo != None:
            self.ceo = modo[0]
            self.cto = modo[1]
            self.mesaDirectiva = modo[2]
            self.jefeDepartamento = modo[3]
            self.empresa = modo[4]
            self.presidente = modo[5]
            self.accionistasMayoritarios = modo[6]
            self.listarObjetos(self)
        else:
            self.crearBase()
