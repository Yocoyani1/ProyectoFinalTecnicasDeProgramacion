# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:48:17 2018

@author: yocoy
"""
import BaseDeDatos as bd
import Ubicacion as ub
import RedesSociales as rs
import ActividadEconomica as ae
import Empresa as em
import Usuario as us
import Buscador as bus
import MenuBusqueda as mb
import CuentaAdministrador as ca
import InformacionDeLaEmpresa as ide
import Estadisticas as es
import Cliente as cl
import Opiniones as op
import Fundaciones as fu
import Capital as cap
import Departamentos as dep
import ImagenesYVideo as iyv
import Instalaciones as ins
import LideresEmpresariales as le

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
    
    nombresClases = ['Ubicacion','RedesSociales','ActividadEconomica','Empresa','Usuario','Buscador','MenuBusqueda','CuentaAdministrador','InformacionDeLaEmpresa','Estadisticas','Cliente','Opiniones','Fundaciones','Capital','Departamentos','ImagenesYVideo','Instalaciones','LideresEmpresariales']
    clases = bd.BaseDeDatos('BaseClases',['nombre'])
    try:
        bd.BaseDeDatos.comprobarDato('BaseClases', 'nombre', 'Usuario')
    except:  
        for clase in nombresClases:
           clases.agregarDatos('BaseClases', [clase], ['nombre'])
            
    ubi = ub.Ubicacion()
    ubi.crearPrevios()
    redes = rs.RedesSociales()
    redes.crearPrevios()
    act = ae.ActividadEconomica()
    act.crearPrevios()
    empr = em.Empresa()
    empr.crearPrevios()
    user = us.Usuario()
    user.crearPrevios()
    busc = bus.Buscador()
    busc.crearPrevios()
    men = mb.MenuBusqueda()
    men.crearPrevios()
    admin = ca.CuentaAdministrador()
    admin.crearPrevios()
    info = ide.InformacionDeLaEmpresa()
    info.crearPrevios()
    esta = es.Estadisticas()
    esta.crearPrevios()
    client = cl.Cliente()
    client.crearPrevios()
    opi = op.Opiniones()
    opi.crearPrevios()
    fun = fu.Fundaciones()
    fun.crearPrevios()
    capi = cap.Capital()
    capi.crearPrevios()
    depart = dep.Departamentos()
    depart.crearPrevios()
    image = iyv.ImagenesYVideo()
    image.crearPrevios()
    instal = ins.Instalaciones()
    instal.crearPrevios()
    lid = le.LideresEmpresariales()
    lid.crearPrevios()
