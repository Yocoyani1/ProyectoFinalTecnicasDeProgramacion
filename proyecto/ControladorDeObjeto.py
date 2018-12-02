# -*- coding: utf-8 -*-
from BaseDeDatos import BaseDeDatos
from Ubicacion import Ubicacion
from RedesSociales import RedesSociales
from ActividadEconomica import ActividadEconomica
from Empresa import Empresa
from Usuario import Usuario
from Buscador import Buscador
from MenuBusqueda import MenuBusqueda
from CuentaAdministrador import CuentaAdministrador
from InformacionDeLaEmpresa import InformacionDeLaEmpresa
from Estadisticas import Estadisticas
from Cliente import Cliente
from Opiniones import Opiniones
from Fundaciones import Fundaciones
from Capital import Capital
from Departamentos import Departamentos
from ImagenesYVideo import ImagenesYVideo
from Instalaciones import Instalaciones
from LideresEmpresariales import LideresEmpresariales


class ControladorDeObjeto():
	

    def crearObjeto(clase):
        nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
        for nombre in nombresClases:
        	if nombre == clase:
        		eval(clase+'(1)')

    def buscaObjeto(clase):
    	nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
    	nombreObjeto = input("Nombre del objeto a buscar: ")
    	for nombre in nombresClases:	
    		if nombre == clase:
    			eval('BaseDeDatos.buscarDato(clase,'+clase+'.regresarArgumentos()[0], nombreObjeto)')

    def borrarObjeto(clase):
        nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
        print('\n\nLista de argumentos')
        eval('print('+clase+'.regresarArgumentos())')
        print('\n')
        argumento = input('Argumento por el que buscar:')
        nombreObjeto = input("Nombre del objeto a eliminar: ")     
        for nombre in nombresClases:
            if clase == nombre:
                BaseDeDatos.borrarDatos(clase,argumento, nombreObjeto)
                nombreObjeto = eval(clase+'.regresarObjeto(argumento,nombreObjeto)')
                eval(clase+'.eliminarObjeto(nombreObjeto)')

    def editarObjeto(clase):
        nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
        for nombre in nombresClases:
	        if clase == nombre:
	            print('\n\nLista de argumentos')
	            eval('print('+clase+'.regresarArgumentos())')
	            print('\n')

	            argumentoABuscar = input('Por que argumento deseas buscar: ')
	            nombreArgumentoObjeto = input("Valor a buscar: ")

	            argumentoEditar = input("Nombre del argumento a editar: ")
	            nuevoValor = input("Nuevo dato: ")

	            eval(clase+'.editarArgumento(argumentoEditar,'+clase+'.regresarObjeto(argumentoABuscar, nombreArgumentoObjeto), nuevoValor)')
	            BaseDeDatos.editarDatos(clase, argumentoABuscar, nombreArgumentoObjeto, argumentoEditar, nuevoValor)
	       