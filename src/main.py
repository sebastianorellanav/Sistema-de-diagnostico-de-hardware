###############################################################################################
#######################   Aplicación LPO para un sistema de   #################################
#######################   apoyo en diagnóstico de hardware.   #################################
###############################################################################################
#######################   Autores:                            #################################
#######################   Version: 1                          #################################
#######################   Fecha:                              #################################
###############################################################################################

from pyswip import Prolog

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


    for i in prolog.query("diagnostico(Problema, ['lentitud', 'se reinicia'])"):
        print(i)
