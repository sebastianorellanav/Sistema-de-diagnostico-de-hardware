###############################################################################################
#######################   Aplicación LPO para un sistema de   #################################
#######################   apoyo en diagnóstico de hardware.   #################################
###############################################################################################
#######################   Autores:                            #################################
#######################   Version: 1                          #################################
#######################   Fecha:                              #################################
###############################################################################################
#
from tkinter import *
from prologData import prolog

ventana = Tk()
# variable universales
# Lista con todos los sintomas para armar la query
sintomas=['no enciende','sobrecalentamiento','no entra al SO','pantalla negra','se escucha un sonido al intentar encenderlo', 'aparecen rayas en el monitor','lentitud','los programas no funcionan','apagado repentino','se reinicia','se bloquea', 'el antivirus ha desaparecido','descargas lentas','corrupción de archivos', 'se congela la imagen y no responde el sistema', 'los videos se reproducen a tirones o se detienen', 'tarda mucho al abrir archivos', 'conecto un pendrive pero lo reconoce', 'no tengo salida de audio', 'mi pc se enciende solo', 'aparecen constantemente anuncios mientras navego por internet', 'no puedo guardar nuevos archivos', 'mis archivos se borran de forma repentina']
# Lista que indica si un sintoma fue seleccionado o no
estado=[]

def inicializarVariables():
    i=0
    while i<len(sintomas):
        estado.append(0)
        i+=1

#####################
# cambia los estaodos 
def CambioEstado(index):
    if(estado[index]==0):
        estado[index]=1
    else:
        estado[index]=0
# Funcion para mostrar los resultados
def buscarProblemas():
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
    mostrarProblemas(result)


def iniciarInterfaz():
    #inicio de interfaz
    var = IntVar()
    ventana.geometry("800x460")

    #Barra de menu
    menubar = Menu(ventana)
    ventana.config(menu=menubar)
    filemenu = Menu(menubar)
    helpmenu = Menu(menubar)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Salir", command=ventana.quit)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instrucciones")
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    
    #Titulo
    
    titulo = Label(ventana, text="Bienvenido, al Diagnosticador de Hardware", font=("Arial Bold", 15))
    titulo.grid(column= 0, row = 0, sticky = W, pady=5)
    
    info = Label(ventana, text="Por favor selecciona los sintomas que tiene tu computador:")
    info.grid(column=0, row = 1, sticky = W,pady=10)

    #Checkboxs
    s1=Checkbutton(ventana,text="El computador no enciende",command=lambda:CambioEstado(0))
    s1.deselect()
    s1.grid(column=0, row = 2, sticky = W, padx=5)

    s2=Checkbutton(ventana,text="El computador esta sobrecalentado",command=lambda:CambioEstado(1) )
    s2.deselect()
    s2.grid(column=1, row = 2, sticky = W)

    s3=Checkbutton(ventana,text="El computador logra cargar el sistema operativo",command=lambda:CambioEstado(2) )
    s3.deselect()
    s3.grid(column=0, row = 3, sticky = W, padx=5)

    s4=Checkbutton(ventana,text="La pantalla esta en negro",command=lambda:CambioEstado(3) )
    s4.deselect()
    s4.grid(column=1, row = 3, sticky = W)

    s5=Checkbutton(ventana,text="Se escucha un sonido al intentar encender el computador",command=lambda:CambioEstado(4) )
    s5.deselect()
    s5.grid(column=0, row = 4, sticky = W, padx=5)

    s6=Checkbutton(ventana,text="Hay rayas en el monitor",command=lambda:CambioEstado(5) )
    s6.deselect()
    s6.grid(column=1, row = 4, sticky = W)

    s7=Checkbutton(ventana,text="El computador esta lento",command=lambda:CambioEstado(6) )
    s7.deselect()
    s7.grid(column=0, row = 5, sticky = W, padx=5)

    s8=Checkbutton(ventana,text="Los programas no responden",command=lambda:CambioEstado(7) )
    s8.deselect()
    s8.grid(column=1, row = 5, sticky = W)

    s9=Checkbutton(ventana,text="El computador se apaga repentinamente",command=lambda:CambioEstado(8) )
    s9.deselect()
    s9.grid(column=0, row = 6, sticky = W, padx=5)

    s10=Checkbutton(ventana,text="El computador se reinicia",command=lambda:CambioEstado(9) )
    s10.deselect()
    s10.grid(column=1, row = 6, sticky = W)

    s11=Checkbutton(ventana,text="El computador se bloquea",command=lambda:CambioEstado(10) )
    s11.deselect()
    s11.grid(column=0, row = 7, sticky = W, padx=5)

    s12=Checkbutton(ventana,text="El antivirus desaparecio",command=lambda:CambioEstado(11) )
    s12.deselect()
    s12.grid(column=1, row = 7, sticky = W)

    s13=Checkbutton(ventana,text="El computador descarga muy lento",command=lambda:CambioEstado(12) )
    s13.deselect()
    s13.grid(column=0, row = 8, sticky = W, padx=5)

    s14=Checkbutton(ventana,text="Hay corrupcion de archivos",command=lambda:CambioEstado(13) )
    s14.deselect()
    s14.grid(column=1, row = 8, sticky = W)

    s15=Checkbutton(ventana,text="La imagen se congela y sistema no responde",command=lambda:CambioEstado(14) )
    s15.deselect()
    s15.grid(column=0, row = 9, sticky = W, padx=5)

    s16=Checkbutton(ventana,text="Los videos se reproducen a tirones, a saltos o se detienen",command=lambda:CambioEstado(15) )
    s16.deselect()
    s16.grid(column=1, row = 9, sticky = W)

    s17=Checkbutton(ventana,text="Los archivos tardan mucho tiempo para abrirse",command=lambda:CambioEstado(16) )
    s17.deselect()
    s17.grid(column=0, row = 10, sticky = W, padx=5)

    s18=Checkbutton(ventana,text="Al conectar un prendive, el computador no lo reconoce",command=lambda:CambioEstado(17) )
    s18.deselect()
    s18.grid(column=1, row = 10, sticky = W)

    s19=Checkbutton(ventana,text="Cuando pongo un video o música, no se escucha ningún sonido",command=lambda:CambioEstado(18) )
    s19.deselect()
    s19.grid(column=0, row = 11, sticky = W, padx=5)

    s18=Checkbutton(ventana,text="Luego de apagar mi computador, a veces, se vuelve a encender ",command=lambda:CambioEstado(19) )
    s18.deselect()
    s18.grid(column=1, row = 11, sticky = W)

    s20=Checkbutton(ventana,text="Cuando utilizo el browser aparecen constantemente anuncios ",command=lambda:CambioEstado(20) )
    s20.deselect()
    s20.grid(column=0, row = 12, sticky = W, padx=5)

    s21=Checkbutton(ventana,text="Intento guardar algún archivo en el computador pero no me deja",command=lambda:CambioEstado(21) )
    s21.deselect()
    s21.grid(column=1, row = 12, sticky = W)

    s22=Checkbutton(ventana,text="Mis archivos se borran de manera repentina",command=lambda:CambioEstado(21) )
    s22.deselect()
    s22.grid(column=0, row = 13, sticky = W, padx=5)


    #Boton para consular
    refresh=Button(ventana,text="Consultar",command=lambda: buscarProblemas())
    refresh.grid(column=1, row= 15, sticky = W, pady=15)

    ventana.mainloop()

def mostrarProblemas(result):
    problemas = Tk()
    numResult=len(result)
   	
    if(numResult!=0):
        titulo = Label(problemas, text="Los Posibles problemas de tu computador son:", font=("Arial Bold", 15))
        titulo.grid(column= 0, row = 0, sticky = W, pady=5)
        r = 1
        for j in result:
            p = Label(ventana,text=j['Problema'])
            p.grid(column=0, row=r, sticky=W)
            r+=1
    else:
        titulo = Label(problemas, text="No existen problemas asociados a ese conjunto de sintomas", font=("Arial Bold", 15))
        titulo.grid(column= 0, row = 0, sticky = W, pady=5) 


