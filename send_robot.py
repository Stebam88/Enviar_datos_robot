import socket
import time

HOSTrobot = "10.5.10.40" # LA IP DEL ROBOT
PORTrobot = 30003 # EL PUERTO DEL ROBOT
srobot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TIPO DE SOCKET
srobot.connect((HOSTrobot, PORTrobot)) # CONEXIÓN AL SOCKET DEL ROBOT
time.sleep(2)

with open(r'patheo.txt', 'r') as infile, \
     open(r'patheoClean.txt', 'w') as outfile: # BASICAMENTE LIMPIO UN POQUITO EL ARCHIVO PARA TENER YA EL FORMATO QUE VOY A MANDAR Y LO GUARDO EN OTRO
    data = infile.read()
    #data = data.replace("p[", "")
    #data = data.replace("]","")
    #data = data.replace(",","")
    #data = data.replace("\n","")
    data = data.replace(" ", "")
    outfile.write(data)

f=open("patheoClean.txt", "r") # AHORA QUE TENGO LAS POSICIONES SIMPLEMENTE SE LAS VOY MANDANDO
vposi=[]
puntos=f.readlines()
print(puntos[1].replace("\n", ""))
#movimiento= "movej"+"("+puntos[15].replace("\n","")+", a=1.4, v=1.05)"+"\n" # ESTO CON JOINTS
#movimiento= '"'+"movel"+"("+puntos[15].replace("\n","")+", a=1.4, v=1.05)"+'"'+"\n" # NI PUTA IDEA PERO SI CUELA CUELA
#movimiento= "movep"+"("+puntos[1].replace("\n","")+", v=0.4)"+"\n" # ESTO CON POSES p[]
#movimiento= '"'+"movej"+"("+"get_inverse_kin"+"("+puntos[15].replace("\n","")+")"+", a=1.4, v=1.05)"+'"'+"\n" # UN TIO DECIA QUE LE IBA ASI
#movimiento= "movej"+"("+"get_inverse_kin"+"("+puntos[15].replace("\n","")+")"+", a=1.4, v=1.05)"+"\n"
#srobot.send(movimiento.encode('utf8'))
#print(movimiento)
time.sleep(2)
print('Comienzo del path')
for line in puntos: # VOY MANDANDO LOS PUNTOS POCO A POCO
    #movimiento= "movej"+"("+"get_forward_kin"+"("+line.replace("\n","")+")"+", a=1.4, v=1.05)"+"\n"
    movimiento= "movej"+"("+line.replace("\n", "")+", a=7, v=5)"+"\n"
    #"movej"+"("+line.replace("\n","")+", a=1.4, v=1.05)"+"\n"
    srobot.send(movimiento.encode('utf8'))
    #srobot.send(movimiento)
    time.sleep(0.01)
    #print(movimiento)
time.sleep(2)
#coordenadas=puntos.split()

#for line in coordenadas:
#    vposi.append(line)
#print(vposi[1])
#print(type(vposi))
'''
X=[]
Y=[]
Z=[]
Rx=[]
Ry=[]
Rz=[]

for i in range(0,len(vposi)-1,6):
    X.append(vposi[i])
    Y.append(vposi[i+1])
    Z.append(vposi[i+2])
    Rx.append(vposi[i+3])
    Rx.append(vposi[i+4])
    Rx.append(vposi[i+5])


print(vposi[1])
#print(vposi)
#print(vposi[1].replace(',',''))
#print(type(vposi[1]))
#print(i)
'''