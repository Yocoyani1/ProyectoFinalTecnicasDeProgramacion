# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class Instalaciones():
    
    listaArgumentos = ['centroDeDistribucion','centroDeProduccion','manufactura','ensamble','centroDeInvestigacion','centroDeServicios','atencionAClientes','sucursales','sedes','almacenes']
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
        listas = BaseDeDatos.obtenerDatosTotales('Instalaciones')
        for lista in listas:
            Usuario(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Instalaciones',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.centroDeDistribucion = input('Nombre de Usuario: ')
            self.centroDeProduccion = input('id: ')
            self.manufactura = input('Password: ')
            self.ensamble = input('Correo: ')
            self.centroDeInvestigacion = input('Intereses: ')
            self.centroDeServicios = input('Ocupacion: ')
            self.atencionAClientes = input('Descripcion: ')
            self.sucursales = input('Telefono: ')
            self.sedes = input('Tarjeta de credito: ')
            self.almacenes = input('Nivel de usuario: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Instalaciones', [self.centroDeDistribucion,self.centroDeProduccion,self.manufactura,self.ensamble,self.centroDeInvestigacion,self.centroDeServicios,self.atencionAClientes,self.sucursales,self.sedes,self.almacenes], self.listaArgumentos)
        elif modo != None:
            self.centroDeDistribucion = modo[0]
            self.centroDeProduccion = modo[1]
            self.manufactura = modo[2]
            self.ensamble = modo[3]
            self.centroDeInvestigacion = modo[4]
            self.centroDeServicios = modo[5]
            self.atencionAClientes = modo[6]
            self.sucursales = modo[7]
            self.sedes = modo[8]
            self.almacenes = modo[9]
            self.listarObjetos(self)
        else:
            self.crearBase()
