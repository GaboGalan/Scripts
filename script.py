import subprocess
import http.client

#Definimos la funcion con un parametro host que es la dirección ip
def host_esta_activo(host_a_comprobar): 
    #Se hace un try para resolución de errores
    try:
        #Creamos el comando para mandar el ping al ip que buscamos y guardamos la salida
        resultado = subprocess.check_output(["ping", host_a_comprobar, "-n", "1"])
        #Si no hay errores damos un true que significaria que esta activo, en cambio al tener errores nos regresa un false de inactividad
        return True
    except subprocess.CalledProcessError:
        return False
    
#Funcion para hacer el escaneo en base a el parametro de ip/host que le damos
def escanear_red(host_a_comprobar):
    #Try para errores
    try:
        #Guardamos el escaneo de la ejecución de la herramienta nmap, con parametros de velocidad de escaneo y puertos comunes
        resultado = subprocess.check_output(["C:/Program Files (x86)/Nmap/nmap.exe", "-T4", "-F", host_a_comprobar])
        #la salida la decodicamos a urf8
        return resultado.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar Nmap: {e}"

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
        #Esto es para errores, si no es posible obtener el index

#La función principal va a pedir que se intriduzca una dirección o host para hacer ping
if __name__ == "__main__":
    host_a_comprobar = input("Introduce el nombre de host o la dirección IP: ")
    #Si al mandar llamar el metodo con el parametro de host y nos regresa el true imprimimos un texto de activo
    if host_esta_activo(host_a_comprobar):
        print(f"{host_a_comprobar} está activo.\n")

        #Si esta activo vamos a escanear la red
        resultado_escaneo = escanear_red(host_a_comprobar)
        print("Resultado del escaneo:\n")
        print(resultado_escaneo)

        #Si esta activo vamos a comprobar si podemos obtener el index
        contenido_pagina = obtener_pagina_de_inicio(host_a_comprobar)
    
        #Si la respuesta fue error imprime eso
        if contenido_pagina.startswith("Error"):
            print(contenido_pagina)
        #En cambio, imprime el contenido del index
        else:
            print("Contenido de la página de inicio:\n")
            print(contenido_pagina)

    #Si da false entonces imprimimos no activo
    else:
        print(f"{host_a_comprobar} no está activo.\n")

