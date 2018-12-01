# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class Cliente():
    
    listaArgumentos = ['Edad','EstadoSocieconomico','EstadoCivil','Intereses','Genero','DatosdeContacto','Nombre']
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
        listas = BaseDeDatos.obtenerDatosTotales('Cliente')
        for lista in listas:
            Cliente(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Cliente',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:


            self.Edad=input('Edad')
            self.EstadoSocieconomico=input('Estado Socieconomico')
            self.EstadoCivil=input('Estado Civil')
            self.Intereses=input('Intereses')
            self.Genero=input('Genero')
            self.DatosdeContacto=input('Datos de Contacto')
            self.Nombre=input('Nombre')
            
            BaseDeDatos.agregarDatos('Cliente', [self.Edad,self.EstadoSocieconomico,self.EstadoCivil,self.Intereses,self.Genero,self.DatosdeContacto,self.Nombre], self.listaArgumentos)
       
        elif modo != None:

            self.Edad= modo [0]
            self.EstadoSocieconomico= modo [1]
            self.EstadoCivil= modo [2]
            self.Intereses= modo [3]
            self.Genero= modo [4]
            self.DatosdeContacto= modo [5]
            self.Nombre= modo [6]
            self.listarObjetos(self)

            
        else:
            self.crearBase()
