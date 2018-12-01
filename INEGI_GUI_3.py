#INEGI_GUI

from tkinter import *


import Menu as mn
from BaseDeDatos import BaseDeDatos
from ControladorDeObjeto import ControladorDeObjeto
from funciones import validacionEntera
import funciones as fc

def main():
	fc.crearBases()

	

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
def editar():
	BaseDeDatos.editarDatos(Comando_1)
def mostrar():
	BaseDeDatos.mostrarDatos(Comando_1)
def borrar():
	BaseDeDatos.borrarDatos(Comando_1)
def agregar():
	BaseDeDatos.agregarDatose(Comando_1)

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
	Clase_AE = "ActividadEconomica"
	Editar_AE=Button(Popup_1, text="EDITAR",command = BaseDeDatos.editarDatos(Clase_AE))    #def funcion de editar
	Mostrar_AE= Button(Popup_1, text="MOSTRAR",command = BaseDeDatos.mostrarDatos(Clase_AE))
	Eliminar_AE= Button(Popup_1, text="ELIMINAR",command = BaseDeDatos.borrarDatos(Clase_AE))
	Agregar_AE= Button(Popup_1, text="AGREGAR",command = BaseDeDatos.agregarDatos(Clase_AE))
	Editar_AE.pack()
	Mostrar_AE.pack()
	Eliminar_AE.pack()
	Agregar_AE.pack()

	Popup1=Label(Popup_1,text="Actividad Economica:",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Tipo empresa \nSector economico\n Razon social\nTamano\nExportaciones\nImportaciones\nAsociaciones\nInversionistas\nAccionistas",bg="white")
	Ventana_1.pack(fill=X)

def Capital_1():


	Popup_1=Toplevel()

	Editar_CAP=Button(Popup_1, text="EDITAR",command = editar)    #def funcion de editar
	Mostrar_CAP= Button(Popup_1, text="MOSTRAR",command = mostrar)
	Eliminar_CAP= Button(Popup_1, text="ELIMINAR",command = borrar)
	Agregar_CAP= Button(Popup_1, text="AGREGAR",command = agregar)
	Editar_CAP.pack()
	Mostrar_CAP.pack()
	Eliminar_CAP.pack()
	Agregar_CAP.pack()

	Popup1=Label(Popup_1,text="Capital",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Presupuesto inicial\nGasto anual total\nPrestamos\nRecursos humanos\nRecursos materiales\nAportaciones PIB\nSubsidios\nDonativos\nRelaciones economicas\nListar objetos",bg="white")
	Ventana_1.pack(fill=X)

def Departamentos_1():

	Popup_1=Toplevel()

	Editar_DEP=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_DEP= Button(Popup_1, text="MOSTRAR",command=BaseDeDatos.mostrarDatos(Comando_1))
	Eliminar_DEP= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_DEP= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_DEP.pack()
	Mostrar_DEP.pack()
	Eliminar_DEP.pack()
	Agregar_DEP.pack()

	Popup1=Label(Popup_1,text="Departamentos",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="No. empleados\nInvestigacion\nLogistica\nDistribucion\nRecursos humanos\nReguridad\nFinanzas\nLegal\nVentas\nPublicidad\nAtenciona clientes",bg="white")
	Ventana_1.pack(fill=X)

def Estadisticas_1():

	Popup_1=Toplevel()

	Editar_EST=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_EST= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_EST= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_EST= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_EST.pack()
	Mostrar_EST.pack()
	Eliminar_EST.pack()
	Agregar_EST.pack()

	Popup1=Label(Popup_1,text="Estadisticas",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Opciones comparacion\nGraficos\nInformaciondatos\nResenas\nNo. opiniones\nContrataciones\nDespidos\nTamano de empresa\nCrecimiento",bg="white")
	Ventana_1.pack(fill=X)

def Informacion_de_la_empresa():

	Popup_1=Toplevel()

	Editar_INF=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_INF= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_INF= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_INF= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_INF.pack()
	Mostrar_INF.pack()
	Eliminar_INF.pack()
	Agregar_INF.pack()

	Popup1=Label(Popup_1,text="Informacion de Empresa",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre\nTelefono\nFax\nCarreras\nForos\nConferencias\nNewsletter\nPublicaciones\nPoliticas de privacidad\nFecha de fundacion\nCorreo",bg="white")
	Ventana_1.pack(fill=X)

def Fundacion_1():

	Popup_1=Toplevel()

	Editar_FUN=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_FUN= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_FUN= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_FUN= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_FUN.pack()
	Mostrar_FUN.pack()
	Eliminar_FUN.pack()
	Agregar_FUN.pack()

	Popup1=Label(Popup_1,text="Fundaciones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Nombre\nClave\nContrasena\nIndentificacion seccion\nPuesto\nCodigo postal\nRacha de contribucion\n,Modificacion reciente\nUltima sesion\nUuario normal",bg="white")
	Ventana_1.pack(fill=X)

def Instalaciones_1():

	Popup_1=Toplevel()

	Editar_INS=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_INS= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_INS= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_INS= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_INS.pack()
	Mostrar_INS.pack()
	Eliminar_INS.pack()
	Agregar_INS.pack()

	Popup1=Label(Popup_1,text="Instalaciones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Centro de distribucion\nCentro produccion\nManufactura\nEnsamble\nCentro de investigacion y servicios\nSucursales\nSedes\nAlmacenes",bg="white")
	Ventana_1.pack(fill=X)

def Opiniones_1():

	Popup_1=Toplevel()

	Editar_OP=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_OP= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_OP= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_OP= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_OP.pack()
	Mostrar_OP.pack()
	Eliminar_OP.pack()
	Agregar_OP.pack()

	Popup1=Label(Popup_1,text="Opiniones",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="Numero de Opiniones\nCalificacion\nCompartidos\nMenciones en la WEB\nComentarios\nUsuarios\nFechas\nRespuestas\nComentarios Inadecuados",bg="white")
	Ventana_1.pack(fill=X)

def Redes_Sociales():

	Popup_1=Toplevel()

	Editar_RED=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_RED= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_RED= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_RED= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_RED.pack()
	Mostrar_RED.pack()
	Eliminar_RED.pack()
	Agregar_RED.pack()

	Popup1=Label(Popup_1,text="Redes Sociales",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
	Ventana_1=Label(Popup_1, text="\nFacebook\nTwitter\nInstagram\nLinkedIn\nYoutube\nE-mail\nVentas en linea\nSkype",bg="white")
	Ventana_1.pack(fill=X)

def Ubicacion_1():

	Popup_1=Toplevel()

	Editar_UBI=Button(Popup_1, text="EDITAR",command=ControladorDeObjeto.editarObjeto(Comando_1))    #def funcion de editar
	Mostrar_UBI= Button(Popup_1, text="MOSTRAR",command=ControladorDeObjeto.mostrarDatos(Comando_1))
	Eliminar_UBI= Button(Popup_1, text="ELIMINAR",command=ControladorDeObjeto.borrarObjeto(Comando_1))
	Agregar_UBI= Button(Popup_1, text="AGREGAR",command=ControladorDeObjeto.buscarObjeto(Comando_1))
	Editar_UBI.pack()
	Mostrar_UBI.pack()
	Eliminar_UBI.pack()
	Agregar_UBI.pack()

	Popup1=Label(Popup_1,text="Ubicacion",bg="aquamarine",font= "Helvetica 14 bold")
	Popup1.pack(side=TOP,fill=X)
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

	global Comando_1
	Comando = Elegir_clase.get()

	Comando_1 = Comando

	if Comando_1 == "Actividad Economica":
		Actividad_Economica()

	if Comando_1 =="Capital":
		Capital_1()
		
	if Comando_1 =="Departamentos":
		Departamentos_1()
		
	if Comando_1 =="Estadisticas":
		Estadisticas_1()
		
	if Comando_1 =="Informacion de la Empresa":
		Informacion_de_la_empresa()
		
	if Comando_1 =="Fundaciones":
		Fundacion_1()

	if Comando_1 =="Fundaciones":
		Instalaciones_1()
		
	if Comando_1 =="Opiniones":
		Opiniones_1()

		
	if Comando_1 =="Ubicacion":
		Ubicacion_1()
		
	if Comando_1 =="Redes Sociales":
		Redes_Sociales()

	#else:
	#	Error_0 = Label (Ventana_Con,text="Error!", fg="white", bg="red", font="Helvetica 16").pack(fill=X)
	#	Espacios_0 = Label(Ventana_Con,text="").pack()
	#	Error_1 = Label(Ventana_Con,text="La clase que buscas no existe en la base de datos Intenta de Nuevo").pack() 
	#	Espacios_1 = Label(Ventana_Con,text="").pack()
	#	Cerrar=Button(Ventana_Con, text="Volver a Intentar", command=Ventana_Con.destroy).pack()

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