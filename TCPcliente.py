from socket import *
serverName = "serverIP"
serverPort = 15000

clientSocket = socket(AF_INET, SOCK_STREAM) #especifica que es un socket TCP
clientSocket.connect((serverName,serverPort)) #inicia una conexion TCP entre cliente y servidor

sentence = input("ESCRIBE UNA FRASE: ")
clientSocket.send(sentence.encode()) #envia el mensaje a traves del socket

modifieldSentence = clientSocket.recv(1054) #recibe los paquetes desde internet
print("mensaje del servidor: ", modifieldSentence.decode())
clientSocket.close() #cierra la conexion

print("se cerro la conexion! \n")

print("by @gabix_708 ------------")
