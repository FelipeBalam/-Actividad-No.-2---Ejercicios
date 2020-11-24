import socket
import re
#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) #Máximo de conexiones

print(f"\n\nServer Listening on {ip}:{port}")

salir = False
cont=0
while salir == False:
    conexion, address = socket_server.accept()
    print ("La conexión  ha sido establecida")

    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)

        if message == 'exit':
            message = 'adios'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break
        else:
            #message = 'No entiendo que deseas...'            
            #conexion.send(message.encode())
            #cantidad de vocales
            patron = re.compile('[aeiouAEIOU]')
            for match in re.finditer(patron, message):
                cont=cont+1
            print ("cantidad de vocales: ",cont)
            cont=0

            #cantidad de palabras
            patron = re.compile('[a-zA-Z]+[a-zA-Z]')
            for match in re.finditer(patron, message):
                cont=cont+1
            print ("cantidad de palabras: ",cont)
            cont=0

            #cantidad de numeros
            patron = re.compile(r'\d{1,10}')
            for match in re.finditer(patron, message):
                cont=cont+1
            print ("cantidad de numeros: ",cont)
            cont=0

            #cantidad de palabras que inicien con mayuscula
            patron = re.compile(r'[A-Z]\w+')
            for match in re.finditer(patron, message):
                cont=cont+1
            print ("cantidad de palabras que inicien con mayuscula: ",cont)
            cont=0

            #cantidad de palabras que inicien con mayuscula
            patron = re.compile(r'[a-zA-Z0-9]+[^aeiou]\s')
            for match in re.finditer(patron, message):
                cont=cont+1
            print ("cantidad de palabras que no finalizen con vocal: ",cont)
            cont=0
            conexion.send(message.encode())
        

conexion.close()
print("Servidor Finalizado")
