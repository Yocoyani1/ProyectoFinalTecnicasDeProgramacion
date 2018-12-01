# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Eder
"""
from BaseDeDatos import BaseDeDatos 

class Empresa():
    
    listaArgumentos = ['nombreDeempresa','descripcion','departamentos','posiciones','productosYservicios','legal','numeroDeempleados','mision','vision','recursos','capital']
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
        listas = BaseDeDatos.obtenerDatosTotales('Empresa')
        for lista in listas:
            Empresa(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Empresa',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.nombreDeEmpresasuario = input('Nombre de Empresa: ')
            self.descripcion = input('Descripcion: ')
            self.departamentos = input('Departamentos: ')
            self.posiciones = input('Posiciones: ')
            self.productosYservicios = input('Productos y Servicios: ')
            self.legal = input('legal: ')
            self.numeroDeempleados = input('numeroDeempleados: ')
            self.mision = input('mision: ')
            self.vision = input('vision: ')
            self.recursos = input('recursos: ')
            self.capital = input('capital: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Empresa', [self.nombreDeEmpresa,self.descripcion,self.departamentos,self.posiciones,self.productosYservicios,self.legal,self.numeroDeempleados,self.mision,self.vision,self.recursos,self.capital], self.listaArgumentos)
        elif modo != None:
            self.nombreDeEmpresa = modo[0]
            self.descripcion = modo[1]
            self.deparamentos = modo[2]
            self.posiciones = modo[3]
            self.productosYservicios = modo[4]
            self.legal = modo[5]
            self.numeroDeempleados = modo[6]
            self.mision = modo[7]
            self.vision = modo[8]
            self.recursos = modo[9]
            self.capital = modo[10]

            self.listarObjetos(self)
        else:
            self.crearBase()

