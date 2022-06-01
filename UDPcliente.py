from socket import *
serverName = 'serverIP';  #aqui va la direccion del servidor
serverPort = 15000; #puerto del servidor

clientSocket = socket(AF_INET, SOCK_DGRAM); #crea el socket UDP

other = " "

while other != "N":

    message = input('ESCRIBE UNA FRASE: ');
    clientSocket.sendto(message.encode(),(serverName, serverPort)) #convierte el mensaje a bytes y lo envia por el socket
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #recibe los paquetes desde internet

    print(modifiedMessage.decode())
    other = input("enviar otro mensaje?: (y/N)").upper()

clientSocket.close() #cierra la conexion del socket
print("by @gabix_708 ------------")
