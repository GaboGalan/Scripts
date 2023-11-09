import http.client

#Definir un metodo para obtener el contenido de la pagina web en base al parametro host
def obtener_pagina_de_inicio(host):
    try:
        #Hacemos la conexion por puerto 80 al host y creamos un request obteniendo una respueta
        conexion = http.client.HTTPConnection(host, 80)
        conexion.request("GET", "/")  # Hacer una solicitud GET para obtener la página de inicio
        respuesta = conexion.getresponse()
        
        #Si se da la respuesta se lee el contenido de la pagina, decodificando en utf y retornamos
        if respuesta.status == 200:
            contenido = respuesta.read()
            return contenido.decode('utf-8')
        else:
            return f"Error: {respuesta.status} - {respuesta.reason}"
    except Exception as e:
        return f"Error al obtener la página de inicio: {e}"
        #Esto es para errores

#El principal va a pedir un host y mandar llamar el metodo para hacer el get al host
if __name__ == "__main__":
    host = input("Introduce el nombre de host o dirección IP: ")
    contenido_pagina = obtener_pagina_de_inicio(host)
    
    #Si la respuesta fue error imprime eso
    if contenido_pagina.startswith("Error"):
        print(contenido_pagina)
    #En cambio, imprime el contenido del index
    else:
        print("Contenido de la página de inicio:\n")
        print(contenido_pagina)

