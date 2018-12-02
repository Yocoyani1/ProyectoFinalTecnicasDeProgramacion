# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos 

class Usuario():
    
    listaArgumentos = ['nombreDeUsuario','id','password','correo','intereses','ocupacion','descripcion','telefono','tarjetaDeCredito','nivelDeUsuario']
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
        listas = BaseDeDatos.obtenerDatosTotales('Usuario')
        for lista in listas:
            Usuario(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('Usuario',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.nombreDeUsuario = input('Nombre de Usuario: ')
            self.id = input('id: ')
            self.password = input('Password: ')
            self.correo = input('Correo: ')
            self.intereses = input('Intereses: ')
            self.ocupacion = input('Ocupacion: ')
            self.descripcion = input('Descripcion: ')
            self.telefono = input('Telefono: ')
            self.tarjetaDeCredito = input('Tarjeta de credito: ')
            self.nivelDeUsuario = input('Nivel de usuario: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Usuario', [self.nombreDeUsuario,self.id,self.password,self.correo,self.intereses,self.ocupacion,self.descripcion,self.telefono,self.tarjetaDeCredito,self.nivelDeUsuario], self.listaArgumentos)
        elif modo != None:
            self.nombreDeUsuario = modo[0]
            self.id = modo[1]
            self.password = modo[2]
            self.correo = modo[3]
            self.intereses = modo[4]
            self.ocupacion = modo[5]
            self.descripcion = modo[6]
            self.telefono = modo[7]
            self.tarjetaDeCredito = modo[8]
            self.nivelDeUsuario = modo[9]
            self.listarObjetos(self)
        else:
            self.crearBase()