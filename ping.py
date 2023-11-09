import subprocess

#Definimos la funcion con un parametro host que es la dirección ip
def host_esta_activo(host): 
    #Se hace un try para resolución de errores
    try:
        #Creamos el comando para mandar el ping al ip que buscamos y guardamos la salida
        resultado = subprocess.check_output(["ping", host, "-n", "1"])
        #Si no hay errores damos un true que significaria que esta activo, en cambio al tener errores nos regresa un false de inactividad
        return True
    except subprocess.CalledProcessError:
        return False

#La función principal va a pedir que se intriduzca una dirección o host para hacer ping
if __name__ == "__main__":
    host_a_comprobar = input("Introduce el nombre de host o la dirección IP: ")
    #Si al mandar llamar el metodo con el parametro de host y nos regresa el true imprimimos un texto de activo
    if host_esta_activo(host_a_comprobar):
        print(f"{host_a_comprobar} está activo.")
    #Si da false entonces imprimimos no activo
    else:
        print(f"{host_a_comprobar} no está activo.")


