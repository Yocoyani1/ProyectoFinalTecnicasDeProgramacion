# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:48:17 2018

@author: yocoy
"""
import BaseDeDatos as bd
import CuentaAdministrador as ca
import Buscador as bus
import MenuBusqueda as mb
import Usuario as us

def  validacionEntera(texto, l1, l2):
    while True:
        try:
            opcion = int(input(texto+ '\n-->'))
            if opcion < l1 or opcion > l2:
                print("Opcion no válida, intenta otra vez")
                continue
            break
        except:
            print("Opcion no válida, intenta otra vez")
    return opcion

def crearBases():
    
    nombresClases = ['Usuario','Buscador','MenuBusqueda','CuentaAdministrador']

    #Crea Base de Datos Y LAS TSBLAS en SQL con una conexion
    clases = bd.BaseDeDatos('BaseClases',['nombre'])

    try:
        #Revisa si ese Dato ya exist en la Tabla correspondiente. Especificamente, revisa si en la Tabla "Nombre" se encutra alguien llamado "Usuario"
        bd.BaseDeDatos.comprobarDato('BaseClases', 'nombre', 'Usuario')
    except:
        #aL PARECER A LA TABLA NOMBRE, ESTA GREGANDOSE LAS CLASES QUE YASEHAN CREADO-------------------------------------------------------------------------------
        for clase in nombresClases:
           clases.agregarDatos('BaseClases', [clase], ['nombre'])

    user = us.Usuario()
    user.crearPrevios()
    busc = bus.Buscador()
    busc.crearPrevios()
    men = mb.MenuBusqueda()
    men.crearPrevios()
    admin = ca.CuentaAdministrador()
    admin.crearPrevios()

