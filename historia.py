import time

terminaste = False
hospital = "Carlos del Claro"
parque = "Goya Requiém" 
randomName1 = "Eduardo"
randomName2 = "Cristina"
randomName3 = "Felipe"
randomName4 = "Sofía"
randomName5 = "Dalila"

print("""
MY HISTORY
Eres un detective y debes descubrir quién es el asesino que mató a tanta gente en los últimos años.
Durante tu aventura tomarás decisiones que te llevarán a diferentes caminos.
Estas decisiones son cruciales pues pueden sentenciar tu muerte.

Cabe recalcar que durante el viaje, se presentarán frases que pueden dañar la sensibilidad del lector, por lo que
se recomienda dejar de leer esta historia si eres menor de 12 años.
===========================================================================================================================""")

OK = (input("Escribe OK cuando hayas acabado de leer.\n\n>"))

print()
print("(Cuantos más datos pongas, más personalizada será la historia)\n")
name = (input("Escribe el nombre del protagonista: "))
place = (input("Escribe el país donde suceden los hechos: "))
year = int(input("Escribe el año de cuando suceden los hechos: "))
print()
extra = int(input("Escribe 1 si quieres poner más datos, escribe 0 si no quieres más: "))
print()

if extra == 1:
    randomName1 = (input("Escribe el nombre de un random que aparecerá en la historia: "))
    randomName2 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))
    randomName3 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))
    randomName4 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))
    print()
    extra2 = int(input("Escribe 1 si quieres poner aún más datos, escribe 0 si no quieres más: "))
    print()
    if extra2 == 1:
        hospital = (input("Escribe el nombre de un hospital: "))
        parque = (input("Escribe el nombre de un parque: "))

print(f"""

En un pueblo de {place} ocurren cosas muy extrañas...
""")
time.sleep(4)

print("""
Allí se han reportado numerosos casos de asesinato. 
No se sabe quién es el autor de los hechos.
""")
time.sleep(7)

print("Tu deber es averiguar quién es el que mató a tanta gente y arrestar al asesino.")
time.sleep(7)

aceptar = (input("¿Quieres empezar la investigación?: "))

if aceptar == "si" or aceptar == "Si" or aceptar == "sí" or aceptar == "Sí":
    print(f"Toma {name}, esta es la información que necesitas.")
elif aceptar == "no" or aceptar == "No":
    print(f"Lo siento {name}, debes empezar la investigación.")
else:
    print("Mmmmm, me lo tomaré como que decidiste empezar.")

time.sleep(3)

while terminaste == False:

    print(f"""

    Estos son algunos de los cadáveres que se han encontrado:
    * {randomName1}
    * {randomName2}
    * {randomName3}
    * {randomName4}

    """)

    opc1 = (input("Escribe el nombre de alguna de estas personas para saber que pasó con ellas: "))


    if opc1 == randomName1:
        print(f"""
        Información del cadáver de {randomName1}
        -El cadáver se halló en {year - 2}.
        -La policía lo encontró muerto en el baño de su casa.
        -Tiene un agujero de 8cm de radio en la parte superior del pecho.
        -Cuando unos profesionales del hospital {hospital} se lo llevaron, le hicieron una autopsia y vieron que le faltaba un corazón. """) 
    elif opc1 == randomName2:
        print(f""" 
        Información del cadáver de {randomName2}
        -El cadáver no fué encontrado.
        -Lo unico que se halló fué una gota de sangre en el parque de {parque} en {year}.
        -Esta gota la encontro el perro del alcalde de {place}.
        -Cuando se encontró la gota de sangre, el hospital {hospital} hizo un analisis y descubrieron
        que el que murió se trataba de {randomName2}.""")
     
    elif opc1 == randomName3:
        print(f"""
        Información del cadáver de {randomName3}
        -El cadáver se encontró dentro de un armario en su casa.
        -Su hermana {randomName5} de tan solo 5 años fué la que encontró el cadáver en {year - 1}.
        -El cuerpo parece como si le faltaran organos...""")
    
    elif opc1 == randomName4:
        print(f""" 
        Información del cadáver de {randomName4}
        -El cadáver se encontró enterrado en un patio de una casa en el año {year}.
        -Al sospechar de que {randomName4} estaba desaparecido, la policia empezó a investigar con sus perros su casa
        y se encontraron enterrado su cuerpo sin extremidades.""")
    
    else:
        print("A esta persona no le pasó nada")

    time.sleep(3)

    print()
    terminasteQ = (input("¿Ya te informaste lo suficiente?: "))

    if terminasteQ == "si" or terminasteQ == "Si" or terminasteQ == "sí" or terminasteQ == "Sí":
        terminaste = True
    

