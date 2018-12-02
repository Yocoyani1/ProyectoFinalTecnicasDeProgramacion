# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class CuentaAdministrador():
    
    listaArgumentos = ['nombre','clave','contrasenaPrimerNivel','identificacionSeccion','puesto','codigoDeNivel','rachaDeContribucion','modificacionReciente','ultimaSesion','usuarioNormal']
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
        listas = BaseDeDatos.obtenerDatosTotales('CuentaAdministrador')
        for lista in listas:
            CuentaAdministrador(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('CuentaAdministrador',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.nombre = input('Nombre Admin.: ')
            self.clave = input('Clave: ')
            self.contrasenaPrimerNivel = input('Contraseña de primer nivel: ')
            self.identificacionSeccion = input('Identificacion de seccion: ')
            self.puesto = input('Puesto: ')
            self.codigoDeNivel = input('Codigo de nivel: ')
            self.rachaDeContribucion = input('Racha de contribucion: ')
            self.modificacionReciente = input('Modificacion reciente: ')
            self.ultimaSesion = input('Ultima sesion: ')
            self.usuarioNormal = input('Usuario publico: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('CuentaAdministrador', [self.nombre, self.clave, self.contrasenaPrimerNivel,self.identificacionSeccion,self.puesto,self.codigoDeNivel,self.rachaDeContribucion,self.modificacionReciente,self.ultimaSesion,self.usuarioNormal], self.listaArgumentos)
            print('2')
        elif modo != None:
            self.nombre= modo[0]
            self.clave = modo[1]
            self.contraseñaPrimerNivel = modo[2]
            self.identificacionSeccion = modo[3]
            self.puesto = modo[4]
            self.codigoDeNivel = modo[5]
            self.rachaDeContribucion = modo[6]
            self.modificacionReciente = modo[7]
            self.ultimaSesion = modo[8]
            self.usuarioNormal = modo[9]
            self.listarObjetos(self)
        else:
            self.crearBase()