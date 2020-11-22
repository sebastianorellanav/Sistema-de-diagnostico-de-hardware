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

from pyswip import Prolog

prolog = Prolog()

# Entrada: void
# Salida: void
# Descripción: se inicializan los hechos y reglas de prolog
def iniciarProlog():    
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