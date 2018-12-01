# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:43 2018

@author: Eder
"""
from BaseDeDatos import BaseDeDatos 

class ImagenesYVideo():
    
    listaArgumentos = ['imagenesYvideo','fotosDellugar','logotipo','productos','publicidad','tiposDepublicidad','simulacionDelproductooservicio','conferencias','videosInformativos']
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
        listas = BaseDeDatos.obtenerDatosTotales('ImagenesYVideo')
        for lista in listas:
            imagenesYvideo(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('ImagenesYVideo',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.imagenesYvideo = input('imagenes y video: ')
            self.fotosDellugar = input('fotos: ')
            self.logotipo = input('logotipo: ')
            self.productos = input('productos: ')
            self.publicidad = input('publicidad : ')
            self.tiposDepublicidad = input('tipos de publicidad: ')
            self.simulacionDelproductooservicio = input('Simulacion del producto: ')
            self.conferencias = input('conferencias: ')
            self.videosInformativos = input('videos informativos: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('ImagenesYVideo', [self.imagenesYvideo,self.fotosDellugar,self.logotipo,self.productos,self.publicidad,self.tiposDepublicidad,self.simulacionDelproductooservicio,self.conferencias,self.videosInformativos], self.listaArgumentos)
        elif modo != None:
            self.imagenesYvideo = modo[0]
            self.fotosDellugar = modo[1]
            self.logotipo = modo[2]
            self.productos = modo[3]
            self.publicidad = modo[4]
            self.tiposDepublicidad = modo[5]
            self.simulacionDelproductooservicio = modo[6]
            self.conferencias = modo[7]
            self.videosInformativos = modo[8]
            self.listarObjetos(self)
        else:
            self.crearBase()

