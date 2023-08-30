import machine
import network
from machine import Pin
from machine import Timer
import time
import socket
#==============================================================================
#FRECUENCIA DE MAQUINA
machine.freq()
machine.freq(80000000)
#==============================================================================
#DEFINICION DE PINES
pin2 = Pin(2, Pin.OUT, value=0)
pin17 = Pin(17, Pin.OUT, value=0)
pin18 = Pin(18, Pin.OUT, value=0)
pin19 = Pin(19, Pin.OUT, value=0)
pin21 = Pin(21, Pin.OUT, value=0)
#==============================================================================
#CONFIGURACION Y CONEXION A RED WIFI
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
net_list = wlan.scan()
wlan.isconnected()
#print("NETWORK_LIST: ", net_list, type(net_list[0][0]),type(net_list[0][1]))
nettofind=("Qyurryus","qyurryus7704980")
print("Red a Encontrar... ", nettofind)
while not wlan.isconnected():
    wlan.connect(nettofind[0],nettofind[1])
    time.sleep(0.5)
print("\n*IFCONFIG: "+str(wlan.ifconfig()))
#VARIABLES
g_decoded = "N"
timeCount = 0
#==============================================================================
#CONFIGURACION DE TIMER
tim1 = Timer(3)
tim1.init(mode=Timer.PERIODIC, period=5, callback=lambda t:funcLeer())
#==============================================================================
#DEFINICION DE FUNCION
def funcLeer():
    global g_decoded
    global timeCount
    global pin2, pin17, pin18, pin19, pin21
    #print("Estas timeCount: ",timeCount)
    timeCount+=1
    if timeCount >=15:
        #if str(g_decoded) == "N":
        g_decoded = "N"
        #print("Normal")
        pin2.value(0)
        pin17.value(0)
        pin18.value(0)
        pin19.value(0)
        pin21.value(0)
        timeCount=0
##==============================================================================
#CONFIGURACION SOCKET COMO SERVIDOR TCP/IP
addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
print("addrs: "+str(addr))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = wlan.ifconfig()[0]
server_port = 1234
socket_addr = (server_ip,server_port)
print("HOST INFO : ",socket_addr)
server_socket.bind(socket_addr)
server_socket.listen(5)
print("Escuchando desde el Servidor: ", socket_addr)
#==============================================================================
#INICIO  DE BUCLE PARA LEER LO QUE MANDA EL CLIENTE (PYTHON EN PC) 
while True:
    client_socket, client_addr = server_socket.accept()
    #print("Conexion Establecida desde: ", (client_socket,client_addr))
    #client_socket.send("Hola saludos desde: SERVIDOR")
    client_response = client_socket.recv(2*1024)
    decoded = str(client_response.decode("utf-8"))
    #print("PETICION= " + str(client_response.decode("utf-8")))
    g_decoded = decoded
    
    if g_decoded != "N":
        pin2.value(1)
    if str(g_decoded) == "1":
        #print("UP")
        pin17.value(1)
    if str(g_decoded) == "2":
        #print("DOWN")
        pin18.value(1)
    if str(g_decoded) == "3":
        #print("LEFT")
        pin19.value(1)
    if str(g_decoded) == "4":
        #print("RIGHT")
        pin21.value(1)
    if str(g_decoded) == "5":
        #print("TWIST_LEFT")
        pass
    if str(g_decoded) == "6":
        #print("TWIST_RIGHT")
        pass
    if str(g_decoded) == "7":
        #print("++PWM")
        pass
    if str(g_decoded) == "8":
        #print("--PWM")
        pass
     
    #print("DECODED= " + decoded)
    client_socket.close()  # serversocket.close()