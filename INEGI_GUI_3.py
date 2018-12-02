#INEGI_GUI

from tkinter import *


import Menu as mn
from BaseDeDatos import BaseDeDatos
from ControladorDeObjeto import ControladorDeObjeto
from funciones import validacionEntera
import funciones as fc

def main():
	fc.crearBases()

def editar():
	ControladorDeObjeto.editarObjeto(Comando_1)

def mostrar():
	BaseDeDatos.mostrarDatos(Comando_1)

def borrar():
	ControladorDeObjeto.borrarObjeto(Comando_1)

def agregar():
	ControladorDeObjeto.crearObjeto(Comando_1)



"""
def Busquedaa():
	v3=Toplevel(root)
	b=Button(v3, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	b1= Button(v3, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	b2= Button(v3, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	b3= Button(v3, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	b.pack()
	b1.pack()
	b2.pack()
	b3.pack()
"""

def Clases():
	Ventana_C=Toplevel(root)

	Encabezado=Label(Ventana_C, text="Clases del Programa", bg="aquamarine",font="Helvetica 14 bold")
	Encabezado.pack(fill=X)

	Explicacion=Label(Ventana_C, text="La integracion del proyecto se conformo por medio de 20 clases \n que se crearon para definir cada una de las caracteristicas \ndel programa")
	Explicacion_1=Label(Ventana_C, text="aunque las enfocadas al contenido referido a la base \n de Datos de INEGI con empresas se resumen en:" , fg="white",bg="grey20",font="Helvetica 12")

	Explicacion_2=Label(Ventana_C, text="Actividad Economica \n Capital \n Departamentos \n Estadisticas \n Informacion de la Empresa \n Fundaciones \n Instalaciones \n Opiniones \n Redes Sociales \n Ubicacion")

	Explicacion_3=Label(Ventana_C, text="Las referidas al funcionamiento del programa son:", fg="white",bg="grey20",font="Helvetica 12")

	Explicacion_4=Label(Ventana_C, text="Empresa \n Usuario \n Buscador \n Menu Busqueda \n Cuenta Administrador \n CLiente \n Lideres Empresariales")

	Explicacion.pack()
	Explicacion_1.pack(fill=X)
	Explicacion_2.pack()
	Explicacion_3.pack(fill=X)
	Explicacion_4.pack()





def login():

	Sesion=Tk()

	global Usuario_2, Contrasena_2

	Relleno=Label(Sesion,text="", bg="navy").pack(fill=X)
	Comienzo=Label(Sesion, text="INICIO DE SESION", fg="white",bg="navy", font="Helvetica 16 bold").pack(fill=X)
	Relleno_1=Label(Sesion,text="", bg="navy").pack(fill=X)

	Usuario=Label(Sesion, text="Usuario", bg="white").pack(fill=X)
	Usuario_1= StringVar()
	Recuadro_1= Entry(Sesion, textvariable=Usuario_1).pack()
	Usuario_2=str(Usuario_1.get())

	Relleno_3=Label(Sesion,text="", bg="navy").pack(fill=X)

	Contrasena=Label(Sesion, text="Contrasena", bg="white").pack(fill=X)
	Contrasena_1= StringVar()
	Recuadro_2= Entry(Sesion,show="*", textvariable=Contrasena_1).pack()
	Contrasena_2=str(Contrasena_1.get())


	with open ("Usuario.txt", 'w') as w:
		w.write("Datos de Usuario")
		w.write(Usuario_2)
		w.write(Contrasena_2)

		pass
	
	Relleno_4=Label(Sesion,text="", bg="navy").pack(fill=X)
    
	Submit=Button(Sesion, text="Iniciar sesion", command=Sesion.destroy).pack()

	Sesion.mainloop()



def Datos():


	Mostrar_Datos=Toplevel(root)

	Encabezado_5=Label(Mostrar_Datos, text="Datos de la Sesion Iniciada:\n\n").pack()
	usu=Label(Mostrar_Datos, text= Usuario_2).pack()
	cons=Label(Mostrar_Datos, text= Contrasena_2).pack()



def Actividad_Economica():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Actividad Economica:",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_AE=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_AE= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_AE= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_AE= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_AE.pack(ipadx=50)
	Mostrar_AE.pack(ipadx=41)
	Eliminar_AE.pack(ipadx=42)
	Agregar_AE.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Tipo empresa \nSector economico\n Razon social\nTamano\nExportaciones\nImportaciones\nAsociaciones\nInversionistas\nAccionistas",bg="white")
	Ventana_1.pack(fill=X)

def Capital_1():


	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Capital",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_CAP=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_CAP= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_CAP= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_CAP= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_CAP.pack(ipadx=50)
	Mostrar_CAP.pack(ipadx=41)
	Eliminar_CAP.pack(ipadx=42)
	Agregar_CAP.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Presupuesto inicial\nGasto anual total\nPrestamos\nRecursos humanos\nRecursos materiales\nAportaciones PIB\nSubsidios\nDonativos\nRelaciones economicas\nListar objetos",bg="white")
	Ventana_1.pack(fill=X)


def Departamentos_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Departamentos",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_DEP=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_DEP= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_DEP= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_DEP= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_DEP.pack(ipadx=50)
	Mostrar_DEP.pack(ipadx=41)
	Eliminar_DEP.pack(ipadx=42)
	Agregar_DEP.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="No. empleados\nInvestigacion\nLogistica\nDistribucion\nRecursos humanos\nReguridad\nFinanzas\nLegal\nVentas\nPublicidad\nAtenciona clientes",bg="white")
	Ventana_1.pack(fill=X)


def Estadisticas_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Estadisticas",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_EST=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_EST= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_EST= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_EST= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_EST.pack(ipadx=50)
	Mostrar_EST.pack(ipadx=41)
	Eliminar_EST.pack(ipadx=42)
	Agregar_EST.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Opciones comparacion\nGraficos\nInformaciondatos\nResenas\nNo. opiniones\nContrataciones\nDespidos\nTamano de empresa\nCrecimiento",bg="white")
	Ventana_1.pack(fill=X)

def Informacion_de_la_empresa():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Informacion de la empresa",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_INF=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_INF= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_INF= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_INF= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_INF.pack(ipadx=50)
	Mostrar_INF.pack(ipadx=41)
	Eliminar_INF.pack(ipadx=42)
	Agregar_INF.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Nombre\nTelefono\nFax\nCarreras\nForos\nConferencias\nNewsletter\nPublicaciones\nPoliticas de privacidad\nFecha de fundacion\nCorreo",bg="white")
	Ventana_1.pack(fill=X)

def Fundacion_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Fundaciones",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_FUN=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_FUN= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_FUN= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_FUN= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_FUN.pack(ipadx=50)
	Mostrar_FUN.pack(ipadx=41)
	Eliminar_FUN.pack(ipadx=42)
	Agregar_FUN.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Nombre\nClave\nContrasena\nIndentificacion seccion\nPuesto\nCodigo postal\nRacha de contribucion\n,Modificacion reciente\nUltima sesion\nUuario normal",bg="white")
	Ventana_1.pack(fill=X)

def Instalaciones_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Instalaciones",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_INS=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_INS= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_INS= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_INS= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_INS.pack(ipadx=50)
	Mostrar_INS.pack(ipadx=41)
	Eliminar_INS.pack(ipadx=42)
	Agregar_INS.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Centro de distribucion\nCentro produccion\nManufactura\nEnsamble\nCentro de investigacion y servicios\nSucursales\nSedes\nAlmacenes",bg="white")
	Ventana_1.pack(fill=X)


def Opiniones_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Opiniones",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_OP=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_OP= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_OP= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_OP= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_OP.pack(ipadx=50)
	Mostrar_OP.pack(ipadx=41)
	Eliminar_OP.pack(ipadx=42)
	Agregar_OP.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Numero de Opiniones\nCalificacion\nCompartidos\nMenciones en la WEB\nComentarios\nUsuarios\nFechas\nRespuestas\nComentarios Inadecuados",bg="white")
	Ventana_1.pack(fill=X)

def Redes_Sociales():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Redes Sociales",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_RED=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_RED= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_RED= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_RED= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_RED.pack(ipadx=50)
	Mostrar_RED.pack(ipadx=41)
	Eliminar_RED.pack(ipadx=42)
	Agregar_RED.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="\nFacebook\nTwitter\nInstagram\nLinkedIn\nYoutube\nE-mail\nVentas en linea\nSkype",bg="white")
	Ventana_1.pack(fill=X)
def Ubicacion_1():

	Popup_1=Toplevel()

	Popup1=Label(Popup_1,text="Ubicacion",bg="steelblue1",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)


	Editar_UBI=Button(Popup_1, text="EDITAR",command = editar, bg="white", fg="navy", font="Helvetica 12 bold")    #def funcion de editar
	Mostrar_UBI= Button(Popup_1, text="MOSTRAR",command = mostrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Eliminar_UBI= Button(Popup_1, text="ELIMINAR",command = borrar, bg="white", fg="navy", font="Helvetica 12 bold")
	Agregar_UBI= Button(Popup_1, text="AGREGAR",command = agregar, bg="white", fg="navy", font="Helvetica 12 bold")

	Editar_UBI.pack(ipadx=50)
	Mostrar_UBI.pack(ipadx=41)
	Eliminar_UBI.pack(ipadx=42)
	Agregar_UBI.pack(ipadx=40)

	space=Label(Popup_1, text="-----------------------------------", bg="steelblue1").pack(fill=X)

	Ventana_1=Label(Popup_1, text="Pais\nEstado\nMunicipio\nLocalidad\nCalle\nNnumero\nCP\nCoordenadas\nSucursales\nArea geografica",bg="white")
	Ventana_1.pack(fill=X)


def CuentaAdmin():
	print("Clase Cuenta de Administrador")


def Atributos():
	Ventana_A=Toplevel(root)

	Encabezado=Label(Ventana_A, text="Atributos del Programa", bg="aquamarine",font="Helvetica 14 bold")
	Encabezado.pack(fill=X)

	Explicacion_5=Label(Ventana_A, text="Con respecto a los atributos del programa, estos fueron")
	Explicacion_6=Label(Ventana_A, text="definidos en cada clase, tomando en cuenta los parametros")
	Explicacion_7=Label(Ventana_A, text="que se podian agregar a cada uno, intentando que cada uno")
	Explicacion_8=Label(Ventana_A, text="de ellos nos diera mas informacion sobre la empresa que se")
	Explicacion_9=Label(Ventana_A, text="creaba y una forma de analizar esa informacion estadisticamente")

	Explicacion_5.pack()
	Explicacion_6.pack()
	Explicacion_7.pack()
	Explicacion_8.pack()
	Explicacion_9.pack()


def Tecnicas_Prog():
	print("Profesor: Emiliavo Nava")
	print("Grupo 2")
	print("Horario: \n Lunes: 7:00 - 9:00 \n Miercoles: 7:00 - 9:00 \n Viernes 7:00 - 9:00")
	print("Semestre: 2019-1")
def Referencias():
	print("URL: http://www.beta.inegi.org.mx/temas/directorio/")

def MenuBusqueda():
	print("Clase Menu Busqueda")

def Lideres():
	print("Clase Lideres Empresariales")

def Tecnicas_Prog():

	Tecnicas_1=Toplevel(root)
	Profesor=Label(Tecnicas_1, text="Profesor: Emiliavo Nava")
	Profesor.pack()
	Grupo=Label(Tecnicas_1, text="Grupo 2")
	Horario=Label(Tecnicas_1,text="Horario: \n Lunes: 7:00 - 9:00 \n Miercoles: 7:00 - 9:00 \n Viernes 7:00 - 9:00")
	Semestre=Label(Tecnicas_1, text="Semestre: 2019-1")
	Grupo.pack()
	Horario.pack()
	Semestre.pack()

def Atribitos_AE():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Actividad Economica:",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Tipo empresa \nSector economico\n Razon social\nTamano\nExportaciones\nImportaciones\nAsociaciones\nInversionistas\nAccionistas",bg="white")
	Ventana_1.pack(fill=X)

def Atribitos_BUS():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Buscador",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre\nUbicacion\nCategoria\nBuscadorinternet\nSucursales\nFiltros busqueda\nTiempo busqueda\nTubempresas\nTistorial",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_CAP():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Capital",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Presupuesto inicial\nGasto anual total\nPrestamos\nRecursos humanos\nRecursos materiales\nAportaciones PIB\nSubsidios\nDonativos\nRelaciones economicas\nListar objetos",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_CLI():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Cliente",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Edad\nEstado socioeconomico\nEstado civil\nIntereses\nGenero\nDatos contacto\nNombre",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_EMP():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Empresas",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre usuario\nDescripcion\nDepartamentos\nPosiciones\nProductos\nLegal\nNunmero de empleados\nMision\nVision\nRecursos\nCapital",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_EST():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Estadisticas",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Opciones comparacion\nGraficos\nInformaciondatos\nResenas\nNo. opiniones\nContrataciones\nDespidos\nTamano de empresa\nCrecimiento",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_INS():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Instalaciones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Centro de distribucion\nCentro produccion\nManufactura\nEnsamble\nCentro de investigacion y servicios\nSucursales\nSedes\nAlmacenes",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_LID():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Lideres Empresariales",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="CEO\nCTO\nMesa directiva\nJefe De departamento\nEmpresa\nPresidente\nAccionistas mayoritarios",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_IMG():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Imagenes y Video",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Imagenes y video\nFotos del lugar\nLogotipo\nProductos\nPublicidad\nTipos publicidad\nSimulacion del producto\nConferencias\nVideos informativos",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_INFO():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Informacion de Empresa",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre\nTelefono\nFax\nCarreras\nForos\nConferencias\nNewsletter\nPublicaciones\nPoliticas de privacidad\nFecha de fundacion\nCorreo",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_UBI():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Ubicacion",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Pais\nEstado\nMunicipio\nLocalidad\nCalle\nNnumero\nCP\nCoordenadas\nSucursales\nArea geografica",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_RED():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Redes Sociales",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="\nFacebook\nTwitter\nInstagram\nLinkedIn\nYoutube\nE-mail\nVentas en linea\nSkype",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_FUN():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Fundaciones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre\nClave\nContrasena\nIndentificacion seccion\nPuesto\nCodigo postal\nRacha de contribucion\n,Modificacion reciente\nUltima sesion\nUuario normal",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_DEP():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Departamentos",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="No. empleados\nInvestigacion\nLogistica\nDistribucion\nRecursos humanos\nReguridad\nFinanzas\nLegal\nVentas\nPublicidad\nAtenciona clientes",bg="white")
	Ventana_1.pack(fill=X)
def Atribitos_OP():
	Popup_1=Toplevel()
	Popup1=Label(Popup_1,text="Opiniones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Numero de Opiniones\nCalificacion\nCompartidos\nMenciones en la WEB\nComentarios\nUsuarios\nFechas\nRespuestas\nComentarios Inadecuados",bg="white")
	Ventana_1.pack(fill=X)


def Convertir():

	global comando1
	Comando = Elegir_clase.get()
	Ventana_Con=Toplevel()

	Comando_1 = Comando

	if Comando_1 == "Actividad Economica":
		Actividad_Economica()
		Ventana_Con.destroy()

	if Comando_1 =="Capital":
		Capital_1()
		Ventana_Con.destroy()
	if Comando_1 =="Departamentos":
		Departamentos_1()
		Ventana_Con.destroy()
	if Comando_1 =="Estadisticas":
		Estadisticas_1()
		Ventana_Con.destroy()
	if Comando_1 =="Informacion de la Empresa":
		Informacion_de_la_empresa()
		Ventana_Con.destroy()
	if Comando_1 =="Fundaciones":
		Fundacion_1()
		Ventana_Con.destroy()
	if Comando_1 =="Instalaciones":
		Instalaciones_1()
		Ventana_Con.destroy()
	if Comando_1 =="Opiniones":
		Opiniones_1()
		Ventana_Con.destroy()
		
	if Comando_1 =="Ubicacion":
		Ubicacion_1()
		Ventana_Con.destroy()
	if Comando_1 =="Redes Sociales":
		Redes_Sociales()
		Ventana_Con.destroy()

	if Comando_1!="Actividad Economica" and Comando_1!="Capital" and Comando_1!="Departamentos" and Comando_1!="Estadisticas" and Comando_1!="Informacion de la empresa" and Comando_1!="Fundaciones" and Comando_1!="Instalaciones" and Comando_1!="Opiniones" and Comando_1!="Ubicacion" and Comando_1!="Redes Sociales":
		
		Error_0 = Label (Ventana_Con,text="Error!", fg="white", bg="red", font="Helvetica 16").pack(fill=X)
		Espacios_0 = Label(Ventana_Con,text="").pack()
		Error_1 = Label(Ventana_Con,text="La clase que buscas no existe en la base de datos Intenta de Nuevo").pack() 
		Espacios_1 = Label(Ventana_Con,text="").pack()
		Cerrar=Button(Ventana_Con, text="Volver a Intentar", command=Ventana_Con.destroy).pack()

#*******************VENTANA PRINCIPAL*******************************
	
Contrasena_2 = ''
Usuario_2 = 'Aun no hay Datos Registrados'
Comando_1 = ''
main()
root = Tk()
root.title("Instituto Nacional de Estadisticas y Geografia")

foto = PhotoImage(file="inegi.png")
etiqueta= Label(root, image=foto)
etiqueta.pack(side=TOP)


bienvenida= Label(root, text="Bienvenido a la Pagina Oficial del INEGI",bg="grey50",fg="white",  font='Helvetica 14 bold')
bienvenida.pack(side=TOP, fill=X)

modulo= Label(root, text="EMPRESAS",bg="white",fg="navy", font='Helvetica 18 bold')
modulo.pack(side=TOP, fill=X)

menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)

menu.add_cascade(label="Archivo", menu=subMenu1)
subMenu1.add_separator()
subMenu1.add_command(label="Salir", command= root.quit)

subMenu2= Menu(menu)

menu.add_cascade(label="Informacion Proyecto", menu=subMenu2)
subMenu2.add_command(label="Clases", command= Clases )
subMenu2.add_command(label="Atributos", command= Atributos)
subMenu2.add_separator()
subMenu2.add_command(label="Tecnicas de Programacion", command= Tecnicas_Prog)

subMenu3 = Menu(menu)

menu.add_cascade(label="INEGI", menu=subMenu3)
subMenu3.add_command(label="Referencias", command= Referencias)
subMenu3.add_separator()

Inicio= Menu(menu)

menu.add_cascade(label="INICIA SESION", menu=Inicio)
Inicio.add_command(label="Haz Click Aqui", command= login)

#TOOLBAR ****



toolbar = Frame(root, bg="medium aquamarine")

insertar1 = Button(toolbar, text= "Lideres Empresariales", command= Atribitos_LID, bg="white", fg="medium aquamarine")
insertar1.pack(side=LEFT, padx=2, pady=2, ipadx=35)
insertar2 = Button(toolbar, text= "Usuario", command= Datos, bg="white", fg="medium aquamarine")
insertar2.pack(side=RIGHT, padx=2, pady=2, ipadx=65)
insertar3 = Button(toolbar, text= "Cliente", command= Atribitos_CLI, bg="white", fg="medium aquamarine")
insertar3.pack(side=RIGHT, padx=2, pady=2, ipadx=65)
insertar4 = Button(toolbar, text= "Imagenes y Video", command= Atribitos_IMG, bg="white", fg="medium aquamarine")
insertar4.pack(side=LEFT, padx=2, pady=2, ipadx=45)

toolbar.pack(side=TOP, fill=X)

espacio = Label(root,text= "")
espacio1 = Label(root,text= "")
espacio2 = Label(root,text= "")
espacio3 = Label(root,text= "")
espacio4 = Label(root,text= "")
espacio5 = Label(root,text= "", bg="medium aquamarine")
espacio6 = Label(root,text= "")

espacio.pack()
elegir = Label (root, text="Escriba la Opcion deseada:", font='Helvetica 14 bold', bg="gray80")
Elegir_clase=StringVar()
opcion = Entry(root, textvariable=Elegir_clase)



elegir.pack(fill=X)#*****************************

espacio1.pack()

opcion.pack()#***************************************

espacio3.pack()

Boton1=Button(root,text="Buscar", fg="white", bg="navy", font="Helvetica 18 bold",command=Convertir)
Boton1.pack(ipadx=65, ipady=2)

espacio4.pack()

espacio5.pack(fill=X)
#************************************

Clase1 = Button(text= "Actividad Economica", command= Atribitos_AE,  bg="aquamarine2")
Clase2 = Button(text= "Capital", command= Atribitos_CAP, bg="white")
Clase3 = Button(text= "Departamentos", command= Atribitos_DEP, bg="aquamarine2")
Clase4 = Button(text= "Estadisticas", command= Atribitos_EST, bg="white")
Clase5 = Button(text= "Informacion de la Empresa", command= Atribitos_INFO, bg="aquamarine2")
Clase6 = Button(text= "Fundaciones", command= Atribitos_FUN, bg="white")
Clase7 = Button(text= "Instalaciones", command= Atribitos_INS, bg="aquamarine2")
Clase8 = Button(text= "Opiniones", command= Atribitos_OP, bg="white")
Clase9 = Button(text= "Redes Sociales", command= Atribitos_RED, bg="aquamarine2")
Clase10 = Button(text= "Ubicacion", command= Atribitos_UBI, bg="white")


espacio6.pack()

Clase1.pack(pady=2, ipadx=20)
Clase2.pack(pady=2, ipadx=65)
Clase3.pack(pady=2, ipadx=38)
Clase4.pack(pady=2, ipadx=49)
Clase5.pack(pady=2, ipadx=1)
Clase6.pack(pady=2, ipadx=48)
Clase7.pack(pady=2, ipadx=47)
Clase8.pack(pady=2, ipadx=57)
Clase9.pack(pady=2, ipadx=41)
Clase10.pack(pady=2, ipadx=59)



espacio8 = Label(root,text= "")
espacio8.pack()

espacio7 = Label(root,text= "", bg="navy")
espacio7.pack(fill=X)

foto1 = PhotoImage(file="inegi.png")
etiqueta1= Label(root, image=foto1)
etiqueta1.pack(side=TOP)

#STATUS BAR****

status = Label(root, text="Todos los Derechos Reservados. Tecnicas de Programacion 2019", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
