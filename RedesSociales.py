# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Fernando
"""
from BaseDeDatos import BaseDeDatos 

class RedesSociales():
    
    listaArgumentos = ['Facebook','Twitter','Instagram','Youtube','LinkedIn','CorreoElectronico','VentasenLinea','Skype']
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
        listas = BaseDeDatos.obtenerDatosTotales('RedesSociales')
        for lista in listas:
            RedesSociales(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls.listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('RedesSociales',self.listaArgumentos)

    def __init__(self, modo = None):

        if modo == 1:
        
            self.Facebook = input('Perfil de Facebook ')
            self.Twitter = input('Usuario de Twitter ')
            self.Instagram = input('Cuenta de Instagram ')
            self.LinkedIn = input('Nombre de Empresa en LinkedIn ')
            self.Youtube = input('Canal de Youtube ')
            self.CorreoElectronico = input('Correo Electronico de Contacto ')
            self.VentasenLinea = input('Pagina WEB de ventas en linea ')
            self.Skype = input('Nombre de Usuario de Skype')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('RedesSociales', [self.Facebook,self.Twitter,self.Instagram,self.LinkedIn,self.Youtube,self.CorreoElectronico,self.VentasenLinea,self.Skype], self.listaArgumentos)

        elif modo != None:

            self.Facebook = modo [0]
            self.Twitter = modo [1]
            self.Instagram = modo [2]
            self.LinkedIn = modo [3]
            self.Youtube = modo [4]
            self.CorreoElectronico = modo [5]
            self.VentasenLinea = modo [6]
            self.Skype = modo [7]
            self.listarObjetos(self)

            
        else:
            self.crearBase()
