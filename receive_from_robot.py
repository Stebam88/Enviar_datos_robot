import socket
import time

HOSTrobot = "10.5.10.40" # LA IP DEL ROBOT
PORTrobot = 30003 # EL PUERTO DEL ROBOT
srobot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TIPO DE SOCKET
srobot.connect((HOSTrobot, PORTrobot)) # CONEXIÓN AL SOCKET DEL ROBOT

HOSTlocal = "10.5.10.250"  # LA IP DEL ORDENADOR
PORTlocal = 6559 # PUERTO DEL ORDENADOR

time.sleep(3)

f = open ("Lectura.script", "rb")  # EL SCRIPT QUE LANZO AL ROBOT

l = f.read(4096)
path = open("patheo.txt", "w") 

while (l):
    srobot.send(l) # SE LO MANDO AL ROBOT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOSTlocal, PORTlocal)) # PONGO EL PUENTE
        s.listen() # ME PONGO A ESCUCHAR
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}") # SIMPLEMENTE PARA QUE ME DE LA INFO DE A QUE ME HE CONECTADO
            while True:
                data = conn.recv(4096) # TODA LA INFORMACION QUE MANDA EL ROBOT
                if not data:
                    break
                conn.sendall(data)
                print(data)
                path = open("patheo.txt", "a") 
                path.write(data.decode("utf-8")) # VOY ESCRIBIENDO EN EL TXT LAS POSES DEL TCP
    l = f.read(4096)
    print(l)
    #slocal.connect((HOSTlocal, PORTlocal))
srobot.close() # HAY QUE CERRAR EL SOCKET DE CONTROL
s.close() # HAY QUE CERRAR EL SOCKET DE ESCUCHA