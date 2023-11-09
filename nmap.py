#Este es un intento de conectar los datos del escaneo a BD con mysql, pero no funciona la implementación
#Parece ser que es por la forma en la que intenté manejar las subcadenas del rresultado del escaneo
#De igual forma abajo esta un codigo comentado de como puedo mandar datos correctamente a la BD 

import subprocess
import mysql.connector

# Conectarse a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

#Escanear la red con un host proporcionado con la herramienta de nmap
def escanear_red(ip_rango):
    try:
        resultado = subprocess.check_output(["C:/Program Files (x86)/Nmap/nmap.exe", "-T4", "-F", ip_rango])
        return resultado.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar Nmap: {e}"

#Guardar el resultado del escaneo mediante las subcadenas obtenidas del split
def guardar_subcadenas(subcadenas):
    cursor = conexion.cursor()

    # Iterar a través de las subcadenas y guardarlas en la base de datos en grupos de 3
    for i in range(0, len(subcadenas), 3):
        if i + 2 < len(subcadenas):
            puerto, estado, servicio = subcadenas[i], subcadenas[i + 1], subcadenas[i + 2]
            #Query a BD con los 3 parametros deseados a guardar
            insert_query = "INSERT INTO escaneo (`Puerto`, `Estado`, `Servicio`) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (puerto, estado, servicio))

    conexion.commit()

#Principal donde se pide la ip/host
if __name__ == "__main":
    ip_rango = input("Introduce el rango de IP a escanear (ejemplo: 192.168.1.1-254): ")
    
    #Resultados del nmap y split para obtener subcadenas
    resultado_escaneo = escanear_red(ip_rango)
    subcadenas = resultado_escaneo.split()
    
    print("Resultado del escaneo:\n")
    print(resultado_escaneo)

    subcadenas = subcadenas[33:]
    print(subcadenas)

    #buscar guardar en la BD
    guardar_subcadenas(subcadenas)
    
    conexion.close()  # Cerrar la conexión a la base de datos al final del programa

"""
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
cursor = conexion.cursor()
subcadena1 = "80"
subcadena2 = "open"
subcadena3 = "http"

insert_query = "INSERT INTO escaneo (`Puerto`, `Estado`, `Servicio`) VALUES (%s,%s,%s)"
cursor.execute(insert_query, (subcadena1,subcadena2, subcadena3,))

conexion.commit()

conexion.close() 
"""