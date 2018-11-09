#EJEMPLO DE ALEX, CHECAR LA DIFERENCIA DE LA LOGICA A COMO YO HICE EL EJERCICIO
#Importo numpy para ver la lista mejor al final; no se necesita para la respuesta final.
import numpy as np
nombres = [
    'María del Rosario Estupiñan Hernández',
    'Ana Gabriela Martinez Martinez',
    'Gabriela Muñoz Pérez',
    'Claudia González Aguirre',
    'Denise Martínez Garcia',
    'Ana Karenina Macías Flores',
    'Roberta Pulido Díaz',
    'Yolanda Eréndira Ibarra Márquez',
    'Carmen Ochoa Escandón',
    'Josefina Salinas Martínez',
    'Hilda María Bañuelos Cortés',
    'Eunice Romero Garza',
    'María Margadalena Sanchez Sanchez',
    'Ana Carolina Junco Treviño',
    'Paula Ivette Durán Rosas',
    'Sandra Maldonado Barrón',
    'Amparo Armendáriz Ruiz',
    'Nadia Leticia Carranza Téllez',
    'Cinthia Ontiveros Garza'
]
#Lo primero que hago es crear una lista de listas con 2 'columnas', una para nombres y otra para apellidos.
NuevoNombre=[['' for x in range(2)] for y in range(len(nombres))]
print(NuevoNombre)
#Comienzo el for, en este caso numeronombre nos da el numero del nombre que estamos cambiando.
for numeronombre in range(len(nombres)):
    #Se divide el nombre
    NombreDiv=nombres[numeronombre].split(' ')
    print(NombreDiv)
    #Se asignan los apellidos a la segunda columna de nuevo nombre
    NuevoNombre[numeronombre][1]=NombreDiv[-2]+' '+NombreDiv[-1]
    #Borramos los apellidos
    del NombreDiv[-1]             #esto es uper fcil y basico! yo lo hice diferente pero asi es mas simple
    del NombreDiv[-1]
    #Asignamos la primera palabra del nombre a la columna de nombres
    NuevoNombre[numeronombre][0]=NombreDiv[0]
    #Comenzamos el for para unir los nombres de la persona.
    for palabra in range(len(NombreDiv)-1):
        NuevoNombre[numeronombre][0]=NuevoNombre[numeronombre][0]+' '+NombreDiv[palabra+1]
#Como np array se imprime mas bonito, convierto la salida en ese formato para ver la lista resultante.
print(np.array(NuevoNombre))
