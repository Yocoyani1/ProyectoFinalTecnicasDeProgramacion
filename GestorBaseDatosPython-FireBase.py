#

from firebase import firebase
url='https://tecnicas-de-pragramacion-o.firebaseio.com/'
default='VACIO'
ListaArgumentos=['Usuarios','Empresa', 'Departamento', 'Cliente']

NombreBase_o='BasePruebas'

class BaseDeDatos():

    # Crea LA BASE DE DATOS Y LAS TABLAS POR CADA CLASE  en SQL
    def __init__(self, nombreBase, argumentos):

        self.nombreBase = nombreBase
        self.argumentos = argumentos

        conexion = firebase.FirebaseApplication(url)
        #Crear un Json donde el nombre, sea el nombre de la
        #  base y los valores, los nombres de las clase
        conexion.put(NombreBase_o, 'Readme', default)

        for args in argumentos:
            conexion.put(nombreBase, args,{str(0):default} )

    @classmethod
    def obtenerDatosTotales(base): #Originalmete tenia "base" en lugar de 'Self'
        conexion = firebase.FirebaseApplication(url)
        listas=conexion.get(url, NombreBase_o)
        return listas

    def mostrarDatos(base):
        conexion = firebase.FirebaseApplication(url)
        listas=conexion.get(url, NombreBase_o)
        print(listas)

    @classmethod
    def PasarArreglos_Json(self, Datos, argumentos, *params):
        json = {}
        i = 0
        for clase in ListaArgumentos:
            if clase in argumentos:
                json[clase] = Datos[i]
                i = i + 1
            else:
                json[clase] = default
        return json

    @classmethod
    def getNumObjBase(self):
        listas = self.obtenerDatosTotales()
        for key in listas:
            NumObj = len(listas[key])
            pass
        return NumObj

    @classmethod
    def agregarDatos(cls, base, datos, argumentos):
        conexion = firebase.FirebaseApplication(url+'/'+NombreBase_o+'/')
        JsonAgregar= cls.PasarArreglos_Json(datos, argumentos)
        id=cls.getNumObjBase()
        print(id,':',JsonAgregar)
        for key in JsonAgregar:
            conexion.put(key, str(id) , JsonAgregar[key])

    def buscarDato(base, argumento, dato):
        conexion = firebase.FirebaseApplication(url)
        lista=conexion.get(NombreBase_o, argumento)
        ListaID=[]
        for ID in range(len(lista)):
            if lista[ID]==dato:
                ListaID.append(ID)
                print(ID, lista[ID])
        return ListaID

        #if dato in lista[]

    def borrarDatos(base, argumento, dato):
        conexion = firebase.FirebaseApplication(url+'/'+NombreBase_o+'/')
        ListaID=base.buscarDato(argumento, dato)

        for ID in ListaID:
            for arg in ListaArgumentos:
                conexion.delete(arg,ID)

    # RERESA TODA LA BASE DE DATOS, OSEA TODAS LAS TABLAS

    def editarDatos(base, argumentoIdentificador, datoIdentificacion, argumentoCambiado, nuevoDato):
        conexion = firebase.FirebaseApplication(url+'/'+NombreBase_o+'/')
        ListaID=base.buscarDato(argumentoIdentificador, datoIdentificacion)
        for ID in ListaID:
            conexion.put(argumentoCambiado, ID,nuevoDato)

    def comprobarDato(base, argumento, dato):
        conexion = firebase.FirebaseApplication(url)
        lista = conexion.get(NombreBase_o, argumento)
        ListaID = []
        for ID in range(len(lista)):
            if lista[ID] == dato:
                ListaID.append(ID)
                print(ID, lista[ID])


bd=BaseDeDatos(NombreBase_o, ListaArgumentos )
#bd.obtenerDatosTotales()
#bd.mostrarDatos()
bd.agregarDatos(NombreBase_o, ['Elena', 'McDonals', 'Telecom','2' ], ['Usuarios','Empresa', 'Departamento'])
bd.agregarDatos(NombreBase_o, ['Joel', 'LoockHeed', 'Jefefe','20%' ], ['Usuarios', 'Departamento', 'Cliente'])
bd.agregarDatos(NombreBase_o, ['McDonals', 'Jfff','230%' ], [ 'Departamento', 'Cliente'])
bd.agregarDatos(NombreBase_o, ['Joel', 'Bombo','0%' ], ['Usuarios', 'Departamento', 'Cliente'])
bd.agregarDatos(NombreBase_o, ['AAAA', 'Bombo', 'fvv','0%' ], ['Usuarios', 'Departamento', 'Cliente'])

bd.borrarDatos('Usuarios', 'Joel')
#bd.mostrarDatos()

bd.editarDatos('Departamento','Bombo', 'Empresa','Coca-cola' )
bd.mostrarDatos()



