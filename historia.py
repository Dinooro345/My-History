import time

hospital = "Carlos del Claro"
randomName1 = "Eduardo"
randomName2 = "Cristina"
randomName3 = "Felipe"
randomName4 = "Sofía"

print()
print("(La info solo influye en la historia así que puedes poner la que usted desee)")
name = (input("Escribe tu nombre: "))
place = (input("Escribe el país donde suceden los hechos: "))
year = int(input("Escribe una fecha de cuando suceden los hechos: "))
extra = int(input("Escribe 1 si quieres poner más datos, escribe 0 si no quieres más: "))

if extra == 1:
    randomName1 = (input("Escribe el nombre de un random que aparecerá en la historia: "))
    randomName2 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))
    randomName3 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))
    randomName4 = (input("Escribe el nombre de otro random que aparecerá en la historia: "))

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



print(f"""

Estos son algunos de los cadáveres que se han encontrado:
* {randomName1}
* Cristina
* Felipe
* Sofía

""")

opc1 = (input("Escribe el nombre de alguna de estas personas para saber que pasó con ellas: "))

if opc1 == randomName1:
    print(f"""
    -El cadáver se halló en {year - 2}
    -La policía lo encontró muerto en el baño de su casa.
    -Tiene un agujero de 8cm de radio en la parte superior del pecho.
    -Cuando unos profesionales del hospital {hospital} se lo llevaron, le hicieron una autopsia y vieron que le faltaba un corazón. """) 
elif opc1 == randomName2:
    print("En este instante, su pizza se está amasando.")
     
elif opc1 == randomName3:
    print("Preparando exquisita pasta...")
    
elif opc1 == randomName1:
    print("Preparando exquisita pasta...")
    
else:
    print("Lo siento, eso no está en el menú")
    

