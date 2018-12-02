# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class ActividadEconomica():
    
    listaArgumentos = ['TipodeEmpresa', 'SectorEconomico', 'RazonSocial', 'Exportaciones','Tamano','Importaciones','Asociaciones','Inversionistas','Accionistas']
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
        listas = BaseDeDatos.obtenerDatosTotales('ActividadEconomica')
        for lista in listas:
            ActividadEconomica(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('ActividadEconomica',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:
            self.TipodeEmpresa=input('Tipo de Empresa:')
            self.SectorEconomico=input('Sector Economico: ')
            self.RazonSocial=input('Razon Social:')
            self.Tamano=input('Tamano de le Empresa:')
            self.Exportaciones=input('Numero de Exportaciones:')
            self.Importaciones=input('Numero de Importaciones: ')
            self.Asociaciones=input('Asociaciones:')
            self.Inversionistas=input('Inversionistas:')
            self.Accionistas=input('Accionistas:')
            BaseDeDatos.agregarDatos('ActividadEconomica', [self.TipodeEmpresa,self.SectorEconomico,self.RazonSocial,self.Exportaciones,self.Importaciones, self.Tamano,self.Asociaciones,self.Inversionistas,self.Accionistas], self.listaArgumentos)
        elif modo != None:
            self.TipodeEmpresa= modo[0]
            self.SectorEconomico= modo[1]
            self.RazonSocial= modo[2]
            self.Tamano= modo[3]
            self.Exportaciones= modo[4]
            self.Importaciones= modo[5]
            self.Asociaciones= modo[6]
            self.Inversionistas= modo[7]
            self.Accionistas= modo[8]
            self.listarObjetos(self)    
        else:
            self.crearBase()
