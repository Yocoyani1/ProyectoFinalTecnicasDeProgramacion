from BaseDeDatos import BaseDeDatos 

class Estadisticas():
    
    listaArgumentos = ['OpcionesComparacion','Graficos','InformacionDatos','Resenias','NumeroOpiniones','Contrataciones','Despidos','TamanioEmpresa','Crecimiento']
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
        listas = BaseDeDatos.obtenerDatosTotales('Estadisticas')
        for lista in listas:
            Estadisticas(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Estadisticas',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.OpcionesComparacion = input('Opciones de comparacion entre empresas: ')
            self.Graficos = input('Graficas de las estadisticas empresariales: ')
            self.InformacionDatos = input('INformacion de los dator empresariales: ')
            self.Resenias = input('Resenias de la empresa: ')
            self.NumeroOpiniones = input('Numero de opiniones: ')
            self.Contrataciones = input('Contraciones anuales: ')
            self.Despidos = input('Despidos anuales: ')
            self.TamanioEmpresa = input('Numero de empleados: ')
            self.Crecimiento = input('Crecimiento anual: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Estadisticas', [self.OpcionesComparacion,self.Graficos,self.InformacionDatos,self.Resenias,self.NumeroOpiniones,self.Contrataciones,self.Despidos,self.TamanioEmpresa,self.Crecimiento], self.listaArgumentos)
        elif modo != None:
            self.OpcionesComparacion = modo[0]
            self.Graficos = modo[1]
            self.InformacionDatos = modo[2]
            self.Resenias = modo[3]
            self.NumeroOpiniones = modo[4]
            self.Contrataciones = modo[5]
            self.Despidos = modo[6]
            self.TamanioEmpresa = modo[7]
            self.Crecimiento = modo[8]
            self.listarObjetos(self)
        else:
            self.crearBase()
