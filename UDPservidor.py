from socket import *
serverPort = 15000
serverSocket = socket(AF_INET,SOCK_DGRAM) #crea el socket UDP

serverSocket.bind(('',serverPort)) #asocial el socket al puerto
print("el servidor UDP esta relisto :D \n")
print("by @gabix_708 ------------")
while True:
       message, clientAddress = serverSocket.recvfrom(2048)
       modifieldMessage = message.decode().upper() #convierte el mensaje a mayusculas
       serverSocket.sendto(modifieldMessage.encode(),clientAddress)
