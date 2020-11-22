###############################################################################################
#######################   Aplicación LPO para un sistema de   #################################
#######################   apoyo en diagnóstico de hardware.   #################################
###############################################################################################
#######################   Autores: Sebastian Orellana         #################################
#######################            Gary Simken                #################################
#######################            Victor Huanqui             #################################
#######################   Version: 2.1                        #################################
#######################   Fecha: 22 Noviembre 2020            #################################
###############################################################################################

# Se importan las librerías a utilizar y se conectan los otros archivos del código
from tkinter import *
from prologData import iniciarProlog
import app

# Main
if __name__ == "__main__":
    iniciarProlog()             # se inicia la base de conocimiento y las reglas
    app.inicializarVariables()  # se inician las variables a utilizar en el programa
    app.iniciarInterfaz()       # se inicializa la interfaz y sus componentes
    