# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:20:07 2018

@author: yocoy
"""
from BaseDeDatos import BaseDeDatos
from ControladorDeObjeto import ControladorDeObjeto
from funciones import validacionEntera

class Menu():
	
    def correr():
        
        while True:
            salir = validacionEntera('Presiona 1 para salir o 2 para continuar', 1, 2)
            if salir == 1:
                break
            BaseDeDatos.mostrarDatos('BaseClases')
            while True:    
                try:
                    clase = input("Nombre de la clase: ")
                    BaseDeDatos.mostrarDatos(clase)
                    break
                except:
                    print('Base no encontrada')

            seleccion = validacionEntera("1)Editar objeto\n2)Eliminar objeto\n3)Buscar objeto\n4)AgregarObjeto", 1,4)
            
            if seleccion == 1:
                try:
                    ControladorDeObjeto.editarObjeto(clase)
                    continue
                except:
                    print('Error al editar el Objeto,\nrevise el argumento a editar o el nombre del objeto')
            
            if seleccion == 2:
                try:
                    ControladorDeObjeto.borrarObjeto(clase)
                    continue
                except:
                    print("Objeto no encontrado")
            
            if seleccion == 3:
                try: 
                    ControladorDeObjeto.buscaObjeto(clase)
                    continue
                except:
                    print('Objeto no encontrado, revisa el nombre')

            if seleccion == 4:
                try:
                    ControladorDeObjeto.crearObjeto(clase)
                    continue
                except:
                    print('Algun dato no fue valido, revisa la entrada')