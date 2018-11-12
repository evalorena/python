import requests
import json
import re  #me ayuda a limpiar mi string, re.sub() ver linea 17 para detalles
import numpy as np

url = 'https://jsonplaceholder.typicode.com/posts/'
#TAREA 1
my_request2 = requests.get(url)
# con esta opción limpiamos el string
datoslimpios= re.sub(' |{|}|\n|;|"', '', my_request2.text)
#aqui corto el string en una lista cada que encuentre una ,
lista =datoslimpios.split(',')
listaindices =[]
for registro in lista:
    if 'id:' in registro or 'title:' in registro:
        listaindices.append(registro)
print(np.array(listaindices)) #pone los dato bonitos
#termina TAREA1

#TAREA2
#itera del 0 al 101 = 100 posiciones
for i in range(101):
    #concatenndo el string de cada url con posts incrementales del 1 al 100
    cadena= "{}{}".format(url,str(i))
    #formdo el url, lo mando llamar
    my_request3 = requests.get(cadena)
    # con esta opción limpiamos el string
    datoslimpios= re.sub(' |{|}|\n|;|"', '', my_request3.text)
    #parto el string en una lista cad elemento separdo por una ,
    cadapost= datoslimpios.split(',')
    for elemento in cadapost:
        if 'title:' in elemento:
            print(elemento)
#termina TAREA2

#AYUDA ALI POR FAVOR
#ESTO NO ES TAREA Casualmente estaba probando a ver si toma el conjunto de datos como diccionario directamente, codigo en stackflow
#pero no me sale, lo toma como lista. que estoy haciendo mal?
dict = {
    "userId": 10,
    "id": 0,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
 }
response = requests.request("GET", url, data=json.dumps(dict))
print(type(response.json()))
#termina mi prueba, aun no queda, lo transforma en lista....

