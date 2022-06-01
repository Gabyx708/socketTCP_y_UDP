from socket import *
serverPort = 15000
serverSocket = socket(AF_INET,SOCK_STREAM) #crea un socket TCP ,este socket es el socket de "bienvenida"

serverSocket.bind(('',serverPort)) #asocia el numero de puerto con el socket
serverSocket.listen(10) #establece el numero maximo de conexiones TCP que acepte el servidor

print("EL TCP SERVIDOR ESTA LISTO :D \n")
print("by @gabix_708 ------------")
while True:
    connectionSocket, addr = serverSocket.accept() #accept crea un socket para cada cliente

    sentece = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentece.upper() #convierte la cadena del mensaje en mayusculas
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close() #cierra la conexion TCP
