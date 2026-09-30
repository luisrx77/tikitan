# class Usuario:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         pass 

#     def saludar (self):
#         print (f"Hola, mi nombre es {self.nombre}")
import requests 

def acortar_url(url):
    endpoint = 'https://cleanuri.com/api/v1/shorten'
    
    data = {"url" : url}
    
    respuesta = requests.post(endpoint, data=data)
    return respuesta.json()["result_url"]
url = input("ingrese la URL que desea acortar: ")
print("la URL acortada es:", acortar_url(url))
