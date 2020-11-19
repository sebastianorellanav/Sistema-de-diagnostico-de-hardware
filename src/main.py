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
    prolog.assertz("sintoma('se congela la imagen y no responde el sistema')")
    prolog.assertz("sintoma('los videos se reproducen a tirones o se detienen')")
    prolog.assertz("sintoma('tarda mucho al abrir archivos')")
    prolog.assertz("sintoma('conecto un pendrive pero lo reconoce')")
    prolog.assertz("sintoma('no tengo salida de audio')")
    prolog.assertz("sintoma('mi pc se enciende solo')")
    prolog.assertz("sintoma('aparecen constantemente anuncios mientras navego por internet')")
    prolog.assertz("sintoma('no puedo guardar nuevos archivos')")
    prolog.assertz("sintoma('mis archivos se borran de forma repentina')")


    prolog.assertz("problema('Virus')")
    prolog.assertz("problema('Falla en la RAM')")
    prolog.assertz("problema('Falla en la placa madre')")
    prolog.assertz("problema('Falla de drivers')")
    prolog.assertz("problema('Falla en la tarjeta gráfica')")
    prolog.assertz("problema('Falla en el Sistema de refrigeración')")
    prolog.assertz("problema('Falla en la memoria física (disco duro)')")
    prolog.assertz("problema('La fuente de alimentación no está conectada o presenta alguna falla')")


    prolog.assertz("relacion('La fuente de alimentación no está conectada o presenta alguna falla', 'no enciende')")
    prolog.assertz("relacion('Falla en la tarjeta gráfica', 'pantalla negra')")
    prolog.assertz("relacion('Falla en la tarjeta gráfica', 'se escucha un sonido al intentar encenderlo')")
    prolog.assertz("relacion('Falla en la tarjeta gráfica', 'aparecen rayas en el monitor')")
    prolog.assertz("relacion('Falla en el Sistema de refrigeración'.'sobrecalentamiento')")
    prolog.assertz("relacion('Falla en el Sistema de refrigeración'.'apagado repentino')")
    prolog.assertz("relacion('Virus', 'lentitud')")
    prolog.assertz("relacion('Virus', 'los programas no funcionan')")
    prolog.assertz("relacion('Virus', 'se reinicia')")
    prolog.assertz("relacion('Virus', 'se bloquea')")
    prolog.assertz("relacion('Virus', 'el antivirus ha desaparecido')")
    prolog.assertz("relacion('Virus', 'descargas lentas')")
    prolog.assertz("relacion('Falla en la RAM', 'lentitud')")
    prolog.assertz("relacion('Falla en la RAM', 'se reinicia')")
    prolog.assertz("relacion('Falla en la RAM', 'corrupción de archivos')")
    prolog.assertz("relacion('Falla en la placa madre', 'pantalla negra')")
    prolog.assertz("relacion('Falla en la placa madre', 'se congela la imagen y no responde el sistema')")
    prolog.assertz("relacion('Falla en la tarjeta gráfica', 'los videos se reproducen a tirones o se detienen')")
    prolog.assertz("relacion('Falla en la memoria física (disco duro)', 'tarda mucho al abrir archivos')")
    prolog.assertz("relacion('Falla de drivers', 'conecto un pendrive pero lo reconoce')")
    prolog.assertz("relacion('Falla de drivers', 'no tengo salida de audio')")
    prolog.assertz("relacion('Virus', 'mi pc se enciende solo')")
    prolog.assertz("relacion('Virus', 'aparecen constantemente anuncios mientras navego por internet')")
    prolog.assertz("relacion('Falla en la memoria física (disco duro)', 'no puedo guardar nuevos archivos')")
    prolog.assertz("relacion('Virus', 'mis archivos se borran de forma repentina')")


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
    
    s15=Checkbutton(ventana,text="La imagen se congela y sistema no responde",command=lambda:CambioEstado(14) )
    s15.deselect()
    s15.pack()

    s16=Checkbutton(ventana,text="Los videos se reproducen a tirones, a saltos o se detienen",command=lambda:CambioEstado(15) )
    s16.deselect()
    s16.pack()

    s17=Checkbutton(ventana,text="Los archivos tardan mucho tiempo para abrirse",command=lambda:CambioEstado(16) )
    s17.deselect()
    s17.pack()

    s18=Checkbutton(ventana,text="Al conectar un prendive, el computador no lo reconoce",command=lambda:CambioEstado(17) )
    s18.deselect()
    s18.pack()

    s19=Checkbutton(ventana,text="Cuando pongo un video o música, no se escucha ningún sonido",command=lambda:CambioEstado(18) )
    s19.deselect()
    s19.pack()

    s18=Checkbutton(ventana,text="Luego de apagar mi computador, a veces, se vuelve a encender ",command=lambda:CambioEstado(19) )
    s18.deselect()
    s18.pack()

    s20=Checkbutton(ventana,text="Cuando utilizo el browser aparecen constantemente anuncios y publicidad molestosa",command=lambda:CambioEstado(20) )
    s20.deselect()
    s20.pack()

    s21=Checkbutton(ventana,text="Intento guardar algún archivo en el computador pero no me deja",command=lambda:CambioEstado(21) )
    s21.deselect()
    s21.pack()

    s22=Checkbutton(ventana,text="Mis archivos se borran de manera repentina",command=lambda:CambioEstado(21) )
    s22.deselect()
    s22.pack()


    #Boton para consular
    refresh=Button(ventana,text="Consultar",command=lambda: show()).pack()
    prob=Label(ventana,text="Posibles problemas").pack()
	
    ventana.mainloop()
