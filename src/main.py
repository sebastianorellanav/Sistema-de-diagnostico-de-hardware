###############################################################################################
#######################   Aplicación LPO para un sistema de   #################################
#######################   apoyo en diagnóstico de hardware.   #################################
###############################################################################################
#######################   Autores:                            #################################
#######################   Version: 1                          #################################
#######################   Fecha:                              #################################
###############################################################################################
from tkinter import *
from pyswip import Prolog
######################
#variable universales
#Lista con todos los sintomas para armar la query
sintomas=['no enciende','sobrecalentamiento','no entra al SO','pantalla negra','se escucha un sonido al intentar encenderlo','aparecen rayas en el monitor','lentitud','los programas no funcionan','apagado repentino','se reinicia','se bloquea','el antivirus ha desaparecido','descargas lentas','corrupción de archivos']
#Lista que indica si un sintoma fue seleccionado o no
estado=[]
i=0
while i<len(sintomas):
    estado.append(0)
    i+=1
#####################
#cambia los estaodos 
def CambioEstado(index):
    if(estado[index]==0):
        estado[index]=1
    else:
        estado[index]=0
#Funcion para mostrar los resultados
def show():
    query="diagnostico(Problema, ["
    i=0
    flag=0
    while i<len(sintomas):
        if(estado[i]==1):
            if(flag==1):
            	query=query+","
            query=query+"'"+sintomas[i]+"'"
            flag=1
        i+=1

    query=query+"])"

    result=prolog.query(query)
    result=list(result)
    numResult=len(result)
   	
    if(numResult!=0):
	    for j in result:
	        myLabel=Label(ventana,text=j['Problema']).pack()
    else:
    	myLabel=Label(ventana,text="No existen problemas asociados").pack()   
# Main
if __name__ == "__main__":
    prolog = Prolog()
    
    # Base de Conocimiento
    prolog.assertz("sintoma('no enciende')")
    prolog.assertz("sintoma('sobrecalentamiento')")
    prolog.assertz("sintoma('no entra al SO')")
    prolog.assertz("sintoma('pantalla negra')")
    prolog.assertz("sintoma('se escucha un sonido al intentar encenderlo')")
    prolog.assertz("sintoma('aparecen rayas en el monitor')")
    prolog.assertz("sintoma('lentitud')")
    prolog.assertz("sintoma('los programas no funcionan')")
    prolog.assertz("sintoma('apagado repentino')")
    prolog.assertz("sintoma('se reinicia')")
    prolog.assertz("sintoma('se bloquea')")
    prolog.assertz("sintoma('el antivirus ha desaparecido')")
    prolog.assertz("sintoma('descargas lentas')")
    prolog.assertz("sintoma('corrupción de archivos')")

    prolog.assertz("problema('La fuente de alimentacion no esta conectada o esta mala')")
    prolog.assertz("problema('Falla en la tarjeta grafica')")
    prolog.assertz("problema('Falla en el Sistema de refrigeracion')")
    prolog.assertz("problema('Virus')")
    prolog.assertz("problema('Falla en la RAM')")

    prolog.assertz("relacion('La fuente de alimentacion no esta conectada', 'no enciende')")
    prolog.assertz("relacion('Falla en la tarjeta grafica', 'pantalla negra')")
    prolog.assertz("relacion('Falla en la tarjeta grafica', 'se escucha un sonido al intentar encenderlo')")
    prolog.assertz("relacion('Falla en la tarjeta grafica', 'aparecen rayas en el monitor')")
    prolog.assertz("relacion('Falla en el Sistema de refrigeracion', 'sobrecalentamiento')")
    prolog.assertz("relacion('Falla en el Sistema de refrigeracion', 'apagado repentino')")
    prolog.assertz("relacion('Virus', 'lentitud')")
    prolog.assertz("relacion('Virus', 'los programas no funcionan')")
    prolog.assertz("relacion('Virus', 'se reinicia')")
    prolog.assertz("relacion('Virus', 'se bloquea')")
    prolog.assertz("relacion('Virus', 'el antivirus ha desaparecido')")
    prolog.assertz("relacion('Virus', 'descargas lentas')")
    prolog.assertz("relacion('Falla en la RAM', 'lentitud')")
    prolog.assertz("relacion('Falla en la RAM', 'se reinicia')")
    prolog.assertz("relacion('Falla en la RAM', 'corrupción de archivos')")


    # Reglas
    prolog.assertz("diagnostico(_,[])")
    prolog.assertz("diagnostico(P,[X|Xs]):- relacion(P,X), diagnostico(P,Xs)")


    #inicio de interfaz
    ventana=Tk()
    var=IntVar()
    ventana.geometry("400x500")

    #Checkboxs
    s1=Checkbutton(ventana,text="El computador no enciende",command=lambda:CambioEstado(0))
    s1.deselect()
    s1.pack()


    s2=Checkbutton(ventana,text="El computador esta sobrecalentado",command=lambda:CambioEstado(1) )
    s2.deselect()
    s2.pack()

    s3=Checkbutton(ventana,text="El computador logra cargar el sistema operativo",command=lambda:CambioEstado(2) )
    s3.deselect()
    s3.pack()

    s4=Checkbutton(ventana,text="La pantalla esta en negro",command=lambda:CambioEstado(3) )
    s4.deselect()
    s4.pack()

    s5=Checkbutton(ventana,text="Se escucha un sonido al intentar encender el computador",command=lambda:CambioEstado(4) )
    s5.deselect()
    s5.pack()

    s6=Checkbutton(ventana,text="Hay rayas en el monitor",command=lambda:CambioEstado(5) )
    s6.deselect()
    s6.pack()

    s7=Checkbutton(ventana,text="El computador esta lento",command=lambda:CambioEstado(6) )
    s7.deselect()
    s7.pack()

    s8=Checkbutton(ventana,text="Los programas no responden",command=lambda:CambioEstado(7) )
    s8.deselect()
    s8.pack()

    s9=Checkbutton(ventana,text="El computador se apaga repentinamente",command=lambda:CambioEstado(8) )
    s9.deselect()
    s9.pack()

    s10=Checkbutton(ventana,text="El computador se reinicia",command=lambda:CambioEstado(9) )
    s10.deselect()
    s10.pack()

    s11=Checkbutton(ventana,text="El computador se bloquea",command=lambda:CambioEstado(10) )
    s11.deselect()
    s11.pack()

    s12=Checkbutton(ventana,text="El antivirus desaparecio",command=lambda:CambioEstado(11) )
    s12.deselect()
    s12.pack()

    s13=Checkbutton(ventana,text="El computador descarga muy lento",command=lambda:CambioEstado(12) )
    s13.deselect()
    s13.pack()

    s14=Checkbutton(ventana,text="Hay corrupcion de archivos",command=lambda:CambioEstado(13) )
    s14.deselect()
    s14.pack()



    #Boton para consular
    refresh=Button(ventana,text="Consultar",command=lambda: show()).pack()
    prob=Label(ventana,text="Posibles problemas").pack()
	
    ventana.mainloop()
