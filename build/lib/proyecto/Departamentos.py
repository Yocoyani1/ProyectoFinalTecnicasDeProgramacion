# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class Departamentos():
    
    listaArgumentos = ['NumerodeEmpleados','Investigacion','Logistica','Distribucion','RecursosHumanos','Seguridad','Finanzas','Legal','Ventas','Publicidad','AtencionaCliente']
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
        listas = BaseDeDatos.obtenerDatosTotales('Departamentos')
        for lista in listas:
            Departamentos(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Departamentos',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:
        


            self.NumerodeEmpleados=input('Numero de Empleados')
            self.Investigacion=input('Departamento de Investigacion')
            self.Logistica=input('Departamento de Logistica')
            self.Distribucion=input('Departamento de Distribucion')
            self.RecursosHumanos=input('Departamento de Recursos Humanos')
            self.Seguridad=input('Departamento de Seguridad')
            self.Finanzas=input('Departamento de Finanzas')
            self.Legal=input('Area Legal')
            self.Ventas=input('Departamento de Ventas')
            self.Publicidad=input('Departamento de Publicidad')
            self.AtencionaCliente=input('Atencion al ClienteCliente')

            BaseDeDatos.agregarDatos('Departamentos', [self.NumerodeEmpleados,self.Investigacion,self.Logistica,self.Distribucion,self.RecursosHumanos,self.Publicidad,self.Seguridad,self.Finanzas,self.Legal,self.Ventas,self.AtencionaCliente], self.listaArgumentos)

        elif modo != None:

            self.NumerodeEmpleados= modo [0]
            self.Investigacion= modo [1]
            self.Logistica= modo [2]
            self.Distribucion= modo [3]
            self.RecursosHumanos= modo [4]
            self.Seguridad= modo [5]
            self.Finanzas= modo [6]
            self.Legal= modo [7]
            self.Ventas= modo [8]
            self.Publicidad= modo [9]
            self.AtencionaCliente= modo [10]
            self.listarObjetos(self)

            
        else:
            self.crearBase()
