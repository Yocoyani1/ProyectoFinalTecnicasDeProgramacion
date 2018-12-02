# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class MenuBusqueda():
    
    listaArgumentos = ['Empresas','Sectores','BusquedaEmpresarial','BusquedaEspecializada','CalificaciondeServicios','IniciarSesion', 'MasBuscados', 'BusquedaGeografica','Imagenes']
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
        listas = BaseDeDatos.obtenerDatosTotales('MenuBusqueda')
        for lista in listas:
            MenuBusqueda(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('MenuBusqueda',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:
        

            self.Empresas = input('Listado de Empresas ')
            self.Sectores = input('Empresas por Sector Economico ')
            self.BusquedaEmpresarial = input('Busqueda Empresarial ')
            self.BusquedaEspecializada = input('Busqueda Especializada ')
            self.CalificaciondeServicios = input('Listado de Calificacion de Servicios ')
            self.IniciarSesion = input('Inicio de Sesion ')
            self.MasBuscados = input('Mas Buscados ')
            self.Busquedageografica = input('Busqueda Geografica ')
            self.Imagenes = input('Imagenes ')
            BaseDeDatos.agregarDatos('MenuBusqueda', [self.Empresas,self.Sectores,self.BusquedaEmpresarial,self.BusquedaEspecializada,self.CalificaciondeServicios,self.IniciarSesion,self.MasBuscados,self.BusquedaGeografica,self.Imagenes], self.listaArgumentos)

        
        elif modo != None:

            self.Empresas = modo [0]
            self.Sectores = modo [1]
            self.BusquedaEmpresarial = modo [2]
            self.BusquedaEspecializada = modo [3]
            self.CalificaciondeServicios = modo [4]
            self.IniciarSesion = modo [5]
            self.MasBuscados = modo [6]
            self.Busquedageografica = modo [7]
            self.Imagenes = modo [8]
            self.listarObjetos(self)

        else:
            self.crearBase()
