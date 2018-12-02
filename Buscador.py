from BaseDeDatos import BaseDeDatos 

class Buscador():
    
    listaArgumentos = ['nombreDeLaEmpresa','Ubicacion','Categoria','BuscadorInternet','Sucursales','FiltrosBusqueda','TiempoBusqueda','Subempresas','Historial']
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
        listas = BaseDeDatos.obtenerDatosTotales('Buscador')
        for lista in listas:
            Buscador(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Buscador',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.nombreDeLaEmpresa = input('Nombre de la Empresa a buscar: ')
            self.Ubicacion= input('Ubicacion de la empresa buscada: ')
            self.Categoria = input('Tipo de empresa: ')
            self.BuscadorInternet = input('Motor de busqueda: ')
            self.Sucursales = input('Sucursales: ')
            self.FiltrosBusqueda = input('Filtros de busqueda: ')
            self.TiempoBusqueda = input('Resultados generados en : ')
            self.Subempresas = input('Subempresas: ')
            self.Historial = input('Historial de busquedas relacionadas: ')
            BaseDeDatos.agregarDatos('Buscador', [self.nombreDeLaEmpresa,self.Ubicacion,self.Categoria,self.BuscadorInternet,self.Sucursales,self.FiltrosBusqueda,self.TiempoBusqueda,self.Subempresas,self.Historial], self.listaArgumentos)
        elif modo != None:
            self.nombreDeLaEmpresa = modo[0]
            self.Ubicacion = modo[1]
            self.Categoria = modo[2]
            self.BuscadorInternet = modo[3]
            self.Sucursales = modo[4]
            self.FiltrosBusqueda = modo[5]
            self.TiempoBusqueda = modo[6]
            self.Subempresas = modo[7]
            self.Historial = modo[8]
            self.listarObjetos(self)
        else:
            self.crearBase()
