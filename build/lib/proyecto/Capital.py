from BaseDeDatos import BaseDeDatos 

class Capital():
    
    listaArgumentos = ['PresupuestoInicial','GastoAnualTotal','Prestamos','RecursosHumanos','RecursosMateriales','AportacionPIB','Subsidios','Donativos','RelacionesEconomicas']
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
        listas = BaseDeDatos.obtenerDatosTotales('Capital')
        for lista in listas:
            Capital(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Capital',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.PresupuestoInicial = input('Presupuesto inicial: ')
            self.GastoAnualTotal = input('Gasto aunal total: ')
            self.Prestamos = input('Prestamos realizados y pedidos: ')
            self.RecursosHumanos = input('Recursos humanos: ')
            self.RecursosMateriales = input('Recursos materiales: ')
            self.AportacionPIB = input('Aportacion neta al Producto Interno Bruto: ')
            self.Subsidios = input('Subsidios gubernamentales: ')
            self.Donativos = input('Donativos recibidos: ')
            self.RelacionesEconomicas = input('Relaciones economicas: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Capital', [self.PresupuestoInicial,self.GastoAnualTotal,self.Prestamos,self.RecursosHumanos,self.RecursosMateriales,self.AportacionPIB,self.Subsidios,self.Donativos,self.RelacionesEconomicas], self.listaArgumentos)
        elif modo != None:
            self.PresupuestoInicial = modo[0]
            self.GastoAnualTotal = modo[1]
            self.Prestamos = modo[2]
            self.RecursosHumanos = modo[3]
            self.RecursosMateriales = modo[4]
            self.AportacionPIB = modo[5]
            self.Subsidios = modo[6]
            self.Donativos = modo[7]
            self.RelacionesEconomicas = modo[8]
            self.listarObjetos(self)
        else:
            self.crearBase()
