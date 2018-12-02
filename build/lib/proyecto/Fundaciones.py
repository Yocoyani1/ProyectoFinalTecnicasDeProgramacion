# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class Fundaciones():
    
    listaArgumentos = ['sociales','ecologicas','politicas','finesDeLucro','alcance','recursosDestinados','eventos','recaudaciones']
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
        listas = BaseDeDatos.obtenerDatosTotales('Fundaciones')
        for lista in listas:
            Fundaciones(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Fundaciones',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.sociales = input('Tienes fundaciones sociales: ')
            self.ecologicas= input('Tienes fundaciones ecologicas: ')
            self.politicas = input('Tienes fundaciones politicas: ')
            self.finesDeLucro= input('Tienes fundaciones sin fines de lucro: ')
            self.alcance = input('Alcance: ')
            self.recursosDestinados = input('Recuros destinado: ')
            self.eventos = input('Eventos: ')
            self.recaudaciones = input('RecaudacionesT: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Fundaciones', [self.sociales,self.ecologicas,self.politicas,self.finesDeLucro,self.alcance,self.recursosDestinados,self.eventos,self.recaudaciones], self.listaArgumentos)
        elif modo != None:
            self.sociales= modo[0]
            self.ecologicas = modo[1]
            self.politicas = modo[2]
            self.finesDeLucro = modo[3]
            self.alcance = modo[4]
            self.recursosDestinados = modo[5]
            self.eventos = modo[6]
            self.recaudaciones = modo[7]

            self.listarObjetos(self)
        else:
            self.crearBase()