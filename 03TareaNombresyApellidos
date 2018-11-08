#Ejercicio: Nombres y apellidos.
#A partir de la siguiente lista de nombres genera sublistas donde separes los dos apellidos del nombre,
#independientemente si la persona tiene uno o dos nombres.
#input: Lista de nombres y apellidos cómputo: separar los últimos dos apellidos en una sub-lista, y el
#nombre o nombres en otra sub-lista output: ejemplo ['Ana Gabriel González García], ['Gisel Martínez Cordero']
#debe cambiar a [['Ana Gabriel'],['González García']], [['Gisel'], ['Martínez Cordero']]

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
    'Cinthia Ontiveros Garza',
    'Perla María Pérez del Campo',
    'Ana Carolina de Anda Juárez'
]
solonombres=[]
soloapellidos=[]
print("Lista de nombres completos en 1 solo registro....")
for i, registro in enumerate(nombres):
    print(i,registro)
    nom_separado=registro.split(' ')
    #empieza a construir la cadena de soloapellidos
    #checar por que no detectaba el nom_separado[-2]!='del'
    if nom_separado[-2]=='del' or nom_separado[-2]=='de' or nom_separado[-3]=='del' or nom_separado[-3]=='de':
        soloapellidos.append(nom_separado[-3]+" "+nom_separado[-2]+" "+nom_separado[-1])
    else:
        soloapellidos.append(nom_separado[-2]+" "+nom_separado[-1])
    cadena_nombres=registro.split(soloapellidos[-1])
    solonombres.append(cadena_nombres[0])
print("Lista de apellidos.....")
print(soloapellidos)
print("Lista de nombres.....")
print(solonombres)
