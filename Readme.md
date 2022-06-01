** PROGRAMACION DE SOCKETS TCP Y UDP EN PYTHON **

#introduccion

los siguientes archivos poseen ejemplos extraido del libro "Redes de computadoras Un enfoque descendente 7a Edición" con
leves modificaciones, los mismo se dejan a disposicion del lector para que pueda modificarlos.

los scripts permiten ejecutar una aplicacion que convierte una cadena de caracteres a la misma cadena pero en mayusculas

##instalacion

clone el repositorio en su directorio local y ejecutelo con algun interprete de python

##modo de uso

Antes de cualquier uso:
-en la variables "serverName" debera colocar la IP de la maquina que utilice como servidor
-en las variables "serverPort" coloque cualquier puesto que este por encima del 1024, este puerto sera el que utilice la maquina servidor

	serverName = "serverIP" <- coloque la direccion de su servidor aqui
	serverPort = 15000 <- coloque el puerto que vaya usar aqui

recuerde que en la maquina servidor no es necesario especificar la IP

ejecute el script del servidor primero en su maquina servidor y consecuentemente ejecute el script XXXcliente.py en la maquina que use como cliente

IMPORTANTE: TCPcliente.py solo puede usarse con TCPservidor.py lo mismo ocurre para UDP

made by Gaby , ig: @gabix_708