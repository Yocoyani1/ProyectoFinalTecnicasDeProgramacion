"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class Ubicacion():
    
    listaArgumentos = ['Pais', 'Estado', 'Municipio', 'Localidad', 'Calle', 'Numero', 'CodigoPostal', 'CoordenadasGeograficas','Sucursales','AreaGeografica']
    _listarObjetos = []

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
        listas = BaseDeDatos.obtenerDatosTotales('Ubicacion')
        for lista in listas:
            Ubicacion(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Ubicacion',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:
        

            self.Pais = input('Pais de Origen ')
            self.Estado = input('Estado ')
            self.Municipio = input('Municipio ')
            self.Localidad = input('Localidad ')
            self.Calle = input('Calle ')
            self.Numero = input('Numero Exterior ')
            self.CodigoPostal = input('Codigo Postal ')
            self.CoordenadasGeograficas = input('Coordenada Geograficas de Sede ')
            self.Sucursales = input('Direccion de Sucursales ')
            self.AreaGeografica = input('Area Geografica comercial ')
            BaseDeDatos.agregarDatos('Ubicacion', [self.Pais,self.Estado,self.Municipio,self.Localidad,self.Calle,self.Numero,self.CodigoPostal,self.CoordenadasGeograficas,self.Sucursales,self.AreaGeografica], self.listaArgumentos)

        elif modo != None:

            self.Pais = modo [0]
            self.Estado = modo [1]
            self.Municipio = modo [2]
            self.Localidad = modo [3]
            self.Calle = modo [4]
            self.Numero = modo [5]
            self.CodigoPostal = modo [6]
            self.CoordenadasGeograficas = modo [7]
            self.Sucursales = modo [8]
            self.AreaGeografica = modo [9]
            self.listarObjetos(self)

        else:
            self.crearBase()
